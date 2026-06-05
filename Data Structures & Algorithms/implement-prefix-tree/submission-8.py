class TrieNode:
    def __init__(self):
        self.end = False
        self.subnodes = {}

class PrefixTree:
    def __init__(self):
        self.dummy = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.dummy
        for w in word:
            if not cur.subnodes.get(w, None):
                cur.subnodes[w] = TrieNode()
            cur = cur.subnodes[w]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.dummy
        for w in word:
            if not cur.subnodes.get(w, None):
                return False
            cur = cur.subnodes[w]
        if not cur.end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.dummy
        for w in prefix:
            if not cur.subnodes.get(w, None):
                return False
            cur = cur.subnodes[w]
        return True