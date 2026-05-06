class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        if m == 1:
            return 1

        count_map = defaultdict(int)
        for t in tasks:
            count_map[t] += 1

        freq_tasks = [ (c, t) for t, c in count_map.items() ]
        freq_tasks.sort(reverse = True)

        count, num = freq_tasks[0][0], 0
        for c, t in freq_tasks:
            if c == count:
                num += 1
            else:
                break

        return max(len(tasks), ((count - 1) * (n + 1) + num))