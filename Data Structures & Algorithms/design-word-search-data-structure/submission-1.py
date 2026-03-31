class TrieNode:
    def __init__(self):
        self.exist = False
        self.suf = {}

class WordDictionary:

    def __init__(self):
        self.dummy = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.dummy
        for w in word:
            if w not in cur.suf:
                cur.suf[w] = TrieNode()
            cur = cur.suf[w]
        cur.exist = True

    def search(self, word: str) -> bool:
        
        def dfs(cur, i):
            tmp = cur
            for j in range(i, len(word)):
                if word[j] != '.':
                    n = tmp.suf.get(word[j], None)
                    if not n:
                        return False
                    if j == len(word)-1:
                        return n.exist
                else:
                    if j == len(word) - 1:
                        for v in tmp.suf.values():
                            if v.exist:
                                return True
                        return False

                    for v in tmp.suf.values():
                        if dfs(v, j+1):
                            return True
                    return False
                tmp = n
            return tmp.exist

        return dfs(self.dummy, 0)
        
            
