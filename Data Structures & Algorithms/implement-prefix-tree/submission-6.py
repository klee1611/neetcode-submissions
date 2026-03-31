class TrieNode:
    def __init__(self):
        self.exist = False
        self.suf = [None] * 26

class PrefixTree:

    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.dummy
        for w in word:
            if not cur.suf[ord(w) - ord('a')]:
                cur.suf[ord(w) - ord('a')] = TrieNode()
            cur = cur.suf[ord(w) - ord('a')]
        cur.exist = True

    def search(self, word: str) -> bool:
        cur = self.dummy
        for w in word:
            n = cur.suf[ord(w) - ord('a')]
            if not n:
                return False
            print(w)
            cur = n
        print(cur.exist)
        return True if cur and cur.exist else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.dummy
        for p in prefix:
            n = cur.suf[ord(p) - ord('a')]
            if not n:
                return False
            cur = n
        return True