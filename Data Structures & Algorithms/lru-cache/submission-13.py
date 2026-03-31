class Node:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1

        node = self.cache.get(key)
        if node == self.head:
            return node.value

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if self.tail == node:
            self.tail = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        print('get: ', key, 'head: ', self.head.value, ', tail: ', self.tail.value)
        return node.value

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.size += 1
            self.head = Node(key, value)
            self.tail, self.cache[key] = self.head, self.head
            return

        drop = None
        if self.cache.get(key):
            drop = self.cache.get(key)
        elif self.size == self.capacity:
            drop = self.tail

        if drop:
            self.cache.pop(drop.key)
            self.size -= 1
            if drop.prev:
                drop.prev.next = drop.next
            if drop.next:
                drop.next.prev = drop.prev
            if drop == self.tail:
                self.tail = drop.prev
            if drop == self.head:
                self.head = drop.next

        self.size += 1
        cur = Node(key, value, None, self.head)
        if self.head:
            self.head.prev = cur
        self.head = cur
        self.cache[key] = cur
        if not self.tail:
            self.tail = cur
        print(key, value, 'head: ', self.head.value, ', tail: ', self.tail.value)

        

