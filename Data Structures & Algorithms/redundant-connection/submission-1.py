class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        map = defaultdict(list)
        degree = [0 for i in range(n)]

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])
            degree[e[0]] += 1
            degree[e[1]] += 1

        q = deque()
        visited = set()
        for i in range(n):
            if degree[i] == 1:
                q.append(i)
                visited.add(i)

        while q:
            node = q.popleft()
            for i in map[node]:
                if i in visited:
                    continue
                degree[i] -= 1
                if degree[i] == 1:
                    q.append(i)
                    visited.add(i)

        for e in reversed(edges):
            if e[0] not in visited and e[1] not in visited:
                return e

        return []