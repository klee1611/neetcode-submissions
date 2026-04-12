class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True

        depend = defaultdict(list)
        indegrees = [0] * numCourses
        for c1, c2 in prerequisites:
            depend[c2].append(c1)
            indegrees[c1] += 1

        visited = set()
        q = deque()
        for c, d in enumerate(indegrees):
            if not d:
                q.append(c)
                visited.add(c)

        while q:
            c = q.popleft()
            for c1 in depend[c]:
                indegrees[c1] -= 1
                if not indegrees[c1] and c1 not in visited:
                    q.append(c1)
                    visited.add(c1)

        return len(visited) == numCourses