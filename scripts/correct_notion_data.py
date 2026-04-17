#!/usr/bin/env python3
"""
Notion Data Correction Script

This script corrects existing Notion database entries to use commit date-based
repetition counts instead of submission number-based counts.

It will:
1. Query all existing problems from your Notion database
2. Analyze git history for each problem to get actual practice days
3. Recalculate SM-2 intervals based on real practice frequency
4. Update Notion with corrected data

Run this script once to fix all existing data after implementing the new logic.
"""

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

def get_problem_commit_dates(problem_name):
    """
    Get all unique dates when a problem was committed.
    Returns list of date strings in YYYY-MM-DD format.
    """
    commit_dates = []

    try:
        # Method 1: Search git log for commits with submission pattern in message
        cmd = ["git", "log", "--format=%ai", "--grep", f"{problem_name} - submission-"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        for line in result.stdout.strip().split('\n'):
            if line:
                date_part = line.split()[0]
                commit_dates.append(date_part)

    except subprocess.CalledProcessError as e:
        print(f"Warning: Error searching commit messages for {problem_name}: {e}")

    try:
        # Method 2: Fallback - check file history for submission files
        problem_dir = f"Data Structures & Algorithms/{problem_name}"
        cmd = ["git", "log", "--format=%ai", "--", f"{problem_dir}/submission-*.py"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        for line in result.stdout.strip().split('\n'):
            if line:
                date_part = line.split()[0]
                commit_dates.append(date_part)

    except subprocess.CalledProcessError as e:
        print(f"Warning: Error searching file history for {problem_name}: {e}")

    # Return unique dates, sorted chronologically
    unique_dates = sorted(list(set(commit_dates)))
    return unique_dates

def count_unique_practice_days(problem_name):
    """
    Count the number of unique days a problem was worked on.
    Returns integer count.
    """
    commit_dates = get_problem_commit_dates(problem_name)
    return len(commit_dates)

def calculate_sm2_progressive(actual_practice_days, quality=4):
    """
    Calculate SM-2 values by simulating all practice days from scratch.
    Each unique commit date counts as one practice day.
    Always starts with EF=2.5 for a clean recalculation.
    """
    if actual_practice_days == 0:
        return 0, 2.5, 0

    ef = 2.5
    interval = 0

    for rep in range(1, actual_practice_days + 1):
        if rep == 1:
            interval = 1
        elif rep == 2:
            interval = 6
        else:
            interval = round(interval * ef)

        ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        ef = max(1.3, ef)

    return actual_practice_days, ef, interval

def get_all_notion_problems():
    """
    Get all problems currently stored in the Notion database.
    """
    try:
        problems = []
        has_more = True
        next_cursor = None

        while has_more:
            query_params = {"database_id": NOTION_DATABASE_ID}
            if next_cursor:
                query_params["start_cursor"] = next_cursor

            response = notion.databases.query(**query_params)

            for page in response["results"]:
                problem_title = ""
                if page["properties"].get("Problem", {}).get("title"):
                    problem_title = page["properties"]["Problem"]["title"][0]["text"]["content"]

                if problem_title:
                    problems.append({
                        "id": page["id"],
                        "name": problem_title,
                        "page": page
                    })

            has_more = response.get("has_more", False)
            next_cursor = response.get("next_cursor")

        return problems

    except Exception as e:
        print(f"Error fetching problems from Notion: {e}")
        return []

def correct_problem_data(problem):
    """
    Correct the data for a single problem based on git history.
    """
    problem_name = problem["name"]
    page = problem["page"]
    page_id = problem["id"]

    print(f"\n--- Analyzing {problem_name} ---")

    # Get current values from Notion
    props = page["properties"]
    current_reps = props.get("Repetitions", {}).get("number") or 0
    current_ef = props.get("Easiness Factor", {}).get("number") or 2.5
    current_interval = props.get("Interval", {}).get("number") or 0

    print(f"Current Notion data: Reps={current_reps}, EF={current_ef:.2f}, Interval={current_interval}")

    # Analyze git history
    commit_dates = get_problem_commit_dates(problem_name)
    actual_practice_days = len(commit_dates)

    print(f"Git history: {len(commit_dates)} unique practice days")
    if commit_dates:
        print(f"Practice dates: {', '.join(commit_dates)}")

    # Check if correction is needed
    if actual_practice_days == 0:
        print("⚠️  No git history found - keeping current Notion values")
        return False

    if current_reps == actual_practice_days:
        print("✅ Already correct - no update needed")
        return False

    # Recalculate from scratch — EF always starts at 2.5 for a clean history replay
    new_reps, new_ef, new_interval = calculate_sm2_progressive(actual_practice_days)

    print(f"Corrected values: Reps={new_reps}, EF={new_ef:.2f}, Interval={new_interval}")
    print(f"Changes: Reps {current_reps}→{new_reps}, Interval {current_interval}→{new_interval}")

    # Use the last commit date as the anchor for Next Review (more accurate than "today")
    last_practice_date = datetime.strptime(commit_dates[-1], "%Y-%m-%d").replace(tzinfo=timezone.utc).date()
    next_review_date = (last_practice_date + timedelta(days=new_interval)).isoformat()
    last_solved_date = commit_dates[-1]

    try:
        # Update Notion
        notion.pages.update(
            page_id=page_id,
            properties={
                "Last Solved": {"date": {"start": last_solved_date}},
                "Repetitions": {"number": new_reps},
                "Easiness Factor": {"number": new_ef},
                "Interval": {"number": new_interval},
                "Next Review": {"date": {"start": next_review_date}}
            }
        )
        print(f"✅ Updated successfully - Last solved: {last_solved_date}, Next review: {next_review_date}")
        return True

    except Exception as e:
        print(f"❌ Failed to update: {e}")
        return False

def main():
    print("🔧 Notion Data Correction Script")
    print("=" * 50)
    print("This script will correct existing Notion data based on actual git commit history.")
    print("It will update repetition counts to reflect unique practice days instead of submission numbers.\n")

    # Get all problems from Notion
    print("📋 Fetching all problems from Notion database...")
    problems = get_all_notion_problems()

    if not problems:
        print("❌ No problems found in Notion database or error occurred.")
        return

    print(f"Found {len(problems)} problems in Notion database.\n")

    # Ask for confirmation
    print("⚠️  This will modify your Notion database. Make sure you have a backup!")
    response = input("Do you want to proceed? (y/N): ").strip().lower()

    if response not in ['y', 'yes']:
        print("Operation cancelled.")
        return

    # Process each problem
    updated_count = 0
    skipped_count = 0

    for i, problem in enumerate(problems, 1):
        print(f"\n[{i}/{len(problems)}] Processing: {problem['name']}")

        if correct_problem_data(problem):
            updated_count += 1
        else:
            skipped_count += 1

    # Summary
    print("\n" + "=" * 50)
    print("🎉 Correction Complete!")
    print(f"✅ Updated: {updated_count} problems")
    print(f"⏭️  Skipped: {skipped_count} problems (no changes needed)")
    print(f"📊 Total processed: {len(problems)} problems")

    if updated_count > 0:
        print(f"\n🔄 Your Notion database has been updated with commit date-based intervals!")
        print("The spaced repetition system will now be more accurate based on actual practice frequency.")

if __name__ == "__main__":
    main()