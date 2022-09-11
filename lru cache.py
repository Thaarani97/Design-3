class DLLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLLNode(-1,-1)
        self.tail = DLLNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = collections.defaultdict()
    
    def addNode(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
    
    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def removeLastNode(self):
        node = self.tail.prev
        self.removeNode(node)
        
    def get(self, key: int) -> int: #TC - O(1), #SC - O(capacity)
        if key not in self.hashmap:
            return -1
        else:
            node = self.hashmap[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        
    def put(self, key: int, value: int) -> None: #TC - O(1), #SC - O(capacity)
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.removeNode(node)
            self.addNode(node)
            
        else:
            node = DLLNode(key,value)
            if len(self.hashmap)>= self.capacity:
                lastNodekey = self.tail.prev.key
                self.removeLastNode()
                del self.hashmap[lastNodekey]
            self.hashmap[key] = node
            self.addNode(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)