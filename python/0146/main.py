from typing import Optional, Dict


class Node:
    def __init__(
            self,
            key: int = 0,
            val: int = 0,
            prev: Optional["Node"] = None,
            next: Optional["Node"] = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.node_map: Dict[int, Node] = dict()
        self.capacity = capacity
        self.size = 0
        self.sentinel = Node()
        self.tail = Node(0, 0, self.sentinel, self.sentinel)
        self.sentinel.next = self.tail
        self.sentinel.prev = self.tail

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            self._evict(key)
            self.size -= 1
        if self.size >= self.capacity:
            node = self.tail.prev
            self._evict(node.key)
            self.size -= 1
        new = Node(key, value, self.sentinel, self.sentinel.next)
        self.sentinel.next = new
        new.next.prev = new
        self.node_map[key] = new
        self.size += 1

    def _evict(self, key) -> None:
        if key not in self.node_map:
            return
        node = self.node_map[key]
        del self.node_map[key]
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
