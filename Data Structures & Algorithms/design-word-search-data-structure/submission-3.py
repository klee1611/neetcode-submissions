class TrieNode:
    def __init__(self):
        self.subnodes = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.dummy = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.dummy
        for w in word:
            if not cur.subnodes.get(w, None):
                cur.subnodes[w] = TrieNode()
            cur = cur.subnodes[w]
        cur.end = True

    def search(self, word: str) -> bool:
        def helper(trie_node, word: str) -> bool:
            cur = trie_node
            if len(word) == 1 and word == '.':
                for k, v in cur.subnodes.items():
                    if v.end:
                        return True
                return False

            for i in range(len(word)):
                if word[i] == '.':
                    for k, v in cur.subnodes.items():
                        if helper(v, word[i+1:]):
                            return True
                    return False

                if not cur.subnodes.get(word[i], None):
                    return False
                cur = cur.subnodes[word[i]]
            return cur.end
        return helper(self.dummy, word)