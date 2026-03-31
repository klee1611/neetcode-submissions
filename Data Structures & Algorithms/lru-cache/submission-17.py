class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.dummy_head = Node(0)
        self.dummy_tail = Node(0, 0, self.dummy_head)
        self.dummy_head.next = self.dummy_tail
        self.cache = {}
        self.cap = capacity

    def remove_node(self, node):
        tmp = node.next
        node.next.prev = node.prev
        node.prev.next = tmp
        self.cache.pop(node.key)

    def add_node(self, node):
        tmp = self.dummy_head.next
        tmp.prev = node
        node.next = tmp
        self.dummy_head.next = node
        node.prev = self.dummy_head
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        
        self.remove_node(node)
        self.add_node(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node:
            node = Node(key, value)
        else:
            self.remove_node(node)
            node.val = value
    
        self.add_node(node)

        if len(self.cache) > self.cap:
            self.remove_node(self.dummy_tail.prev)
