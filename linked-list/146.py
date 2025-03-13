class Node:
    def __init__(self, key=0 ,val=0,pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
    
    def insert(self, node):
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head

    def remove(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.map)==self.capacity:
                node = self.tail.pre
                self.remove(node)
                del self.map[node.key]
            new_node = Node(key, value)
            self.map[key]=new_node
            self.insert(new_node)