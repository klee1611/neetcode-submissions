class Solution:

    def encode(self, strs: List[str]) -> str:
        r = str(len(strs)) + "@"
        for s in strs:
            r = r + str(len(s)) + "@" + s
        return r

    def decode(self, s: str) -> List[str]:
        print(s)
        l = 0
        r = []
        
        def read_str_len(l):
            str_len = ""
            while "@" != s[l]:
                str_len = str_len + s[l]
                l = l+1
            print(str_len, l)
            return (int(str_len), l)

        count, l = read_str_len(l)
        l = l+1
        if 0 == count:
            return []

        for i in range(count):
            str_len, l = read_str_len(l)
            if 0 == str_len:
                r.append("")
            else:
                start, end = l+1, l+1+str_len
                r.append(s[start:end])
            print(r)

            l = l+1+str_len
        return r