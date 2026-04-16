import os
import sys
import subprocess
from datetime import datetime, timedelta, timezone
from notion_client import Client

# Initialize Notion Client
NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID")

if not NOTION_API_KEY or not NOTION_DATABASE_ID:
    print("Error: NOTION_API_KEY and NOTION_DATABASE_ID must be set.")
    sys.exit(1)

notion = Client(auth=NOTION_API_KEY)

def get_new_problems_from_commits():
    """
    Parses the recent commit to find newly solved problems.
    In GitHub actions, it's often easier to read commits directly.
    We will pass the base and head commits as arguments or env vars.
    """
    base_commit = os.environ.get("BASE_COMMIT")
    head_commit = os.environ.get("HEAD_COMMIT", "HEAD")

    try:
        if base_commit and head_commit and base_commit != "0000000000000000000000000000000000000000":
            # We want commits from base to head
            cmd = ["git", "log", f"{base_commit}..{head_commit}", "--format=%s"]
        else:
            cmd = ["git", "log", "-1", "--format=%s"]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        messages = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running git log: {e}\n{e.stderr}")
        return []

    problems = []
    for msg in messages:
        # Example format: Add: count-number-of-islands - submission-2
        if msg.startswith("Add: ") and " - submission-" in msg:
            parts = msg[5:].split(" - submission-")
            if len(parts) == 2:
                problem_name = parts[0].strip()
                problems.append(problem_name)

    return list(set(problems)) # unique problems

def query_problem_in_notion(problem_name):
    """
    Query the Notion database to find if the problem already exists.
    """
    try:
        response = notion.databases.query(
            database_id=NOTION_DATABASE_ID,
            filter={
                "property": "Problem",
                "title": {
                    "equals": problem_name
                }
            }
        )
        if response["results"]:
            return response["results"][0]
        return None
    except Exception as e:
        print(f"Error querying Notion for {problem_name}: {e}")
        return None

def calculate_sm2(repetitions, ef, interval, quality=4):
    """
    Calculate the next review interval using the SM-2 algorithm.
    """
    if quality < 3:
        repetitions = 0
        interval = 1
    else:
        repetitions += 1
        if repetitions == 1:
            interval = 1
        elif repetitions == 2:
            interval = 6
        else:
            interval = round(interval * ef)

    ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    ef = max(1.3, ef)

    return repetitions, ef, interval

def sync_problem_to_notion(problem_name):
    print(f"Syncing {problem_name} to Notion...")
    page = query_problem_in_notion(problem_name)

    today_str = datetime.now(timezone.utc).date().isoformat()

    if page:
        # Update existing
        props = page["properties"]

        # safely extract current values
        repetitions = props.get("Repetitions", {}).get("number") or 0
        ef = props.get("Easiness Factor", {}).get("number") or 2.5
        interval = props.get("Interval", {}).get("number") or 0

        # SM-2 calculation
        new_reps, new_ef, new_interval = calculate_sm2(repetitions, ef, interval, quality=4)

        next_review_date = (datetime.now(timezone.utc) + timedelta(days=new_interval)).date().isoformat()

        try:
            notion.pages.update(
                page_id=page["id"],
                properties={
                    "Last Solved": {"date": {"start": today_str}},
                    "Next Review": {"date": {"start": next_review_date}},
                    "Repetitions": {"number": new_reps},
                    "Easiness Factor": {"number": new_ef},
                    "Interval": {"number": new_interval}
                }
            )
            print(f"Updated {problem_name}: Next review in {new_interval} days.")
        except Exception as e:
            print(f"Failed to update {problem_name} in Notion: {e}")

    else:
        # Create new
        new_reps = 1
        new_ef = 2.5
        new_interval = 1
        next_review_date = (datetime.now(timezone.utc) + timedelta(days=new_interval)).date().isoformat()

        try:
            notion.pages.create(
                parent={"database_id": NOTION_DATABASE_ID},
                properties={
                    "Problem": {"title": [{"text": {"content": problem_name}}]},
                    "Last Solved": {"date": {"start": today_str}},
                    "Next Review": {"date": {"start": next_review_date}},
                    "Repetitions": {"number": new_reps},
                    "Easiness Factor": {"number": new_ef},
                    "Interval": {"number": new_interval}
                }
            )
            print(f"Created {problem_name}: Next review in {new_interval} days.")
        except Exception as e:
            print(f"Failed to create {problem_name} in Notion: {e}")

def main():
    problems = get_new_problems_from_commits()
    if not problems:
        print("No new NeetCode submissions found in the recent commits.")
        return

    print(f"Found {len(problems)} solved problems in recent commits: {', '.join(problems)}")
    for problem in problems:
        sync_problem_to_notion(problem)

if __name__ == "__main__":
    main()
