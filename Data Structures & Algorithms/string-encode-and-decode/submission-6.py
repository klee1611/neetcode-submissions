class Solution:
    def encode(self, strs: List[str]) -> str:
        r = str(len(strs)) + "$"
        for s in strs:
            r += str(len(s)) + "$"
            r += s
        return r

    def decode(self, s: str) -> List[str]:
        r = []
        i = 0

        while s[i] != "$":
            i += 1
        r_len = int(s[:i])
        i += 1
        start = i

        for j in range(r_len):
            while s[i] != "$":
                i += 1
            print(s, start, i)
            s_len = int(s[start:i])
            i += 1
            if s_len == 0:
                r.append("")
            else:
                r.append(s[i:i+s_len])
            start = i + s_len
            i = start
        return r
