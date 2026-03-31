class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False

        map = defaultdict(list)
        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        visited = set()
        q = deque()
        q.append((-1, 0))
        while q:
            prev_node, node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for next_node in map[node]:
                if next_node == prev_node:
                    continue
                q.append((node, next_node))
        
        return len(visited) == n