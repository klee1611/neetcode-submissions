class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_d = defaultdict(int)
        for s in s1:
            s1_d[s] += 1

        start = 0
        while start < len(s2):
            if start + len(s1) > len(s2):
                return False

            if s2[start] not in s1_d:
                start += 1
                continue
        
            i = start
            exist = True
            while i < start + len(s1):
                if s2[i] not in s1_d or s1_d[s2[i]] <= 0:
                    exist = False
                    break

                s1_d[s2[i]] -= 1
                i += 1
            if exist:
                print(start, i)
                return True
            for j in range(start, i):
                print('j, ', s2[j])
                s1_d[s2[j]] += 1
            start += 1

        return False