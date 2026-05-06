class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.countdown = capacity

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def append_node(self, node):
        prev_node = self.tail.prev
        node.prev = prev_node
        prev_node.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.remove_node(node)
        self.append_node(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cache:
            node = self.cache[key]

        elif self.countdown == 0:
            node = self.head.next

        if node:
            self.remove_node(node)
            self.cache.pop(node.key)
            self.countdown += 1

        node = Node(key, value)
        self.append_node(node)
        self.countdown -= 1
        self.cache[key] = node
