class Node:
    def __init__(self):
        self.end = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.dummy = Node()

    def addWord(self, word: str) -> None:
        cur = self.dummy
        for i in range(len(word)):
            if word[i] not in cur.next:
                cur.next[word[i]] = Node()
            cur = cur.next[word[i]]
            if i == len(word) - 1:
                cur.end = True

    def search(self, word: str) -> bool:

        def helper(idx, cur):
            if idx == len(word) - 1:
                if word[idx] == ".":
                    for n in cur.next.values():
                        if n.end:
                            return True
                    return False
                if not word[idx] in cur.next:
                    return False
                if cur.next[word[idx]].end:
                    return True
                return False

            if word[idx] == ".":
                for n in cur.next.values():
                    if helper(idx + 1, n):
                        return True
                return False

            if not word[idx] in cur.next:
                return False
            return helper(idx + 1, cur.next[word[idx]])
        
        return helper(0, self.dummy)