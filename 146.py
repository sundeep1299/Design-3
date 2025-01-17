#time :o(n)
#space:o(n)

class Node:
    def __init__(self,key,val):
        self.key = key
        self.value =value
        self.next= self.prev =None


class LRUCache:

    def __init__(self, capacity: int):
        self.map={}
        self.map=capacity
        
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        
        self.lru.next=self.mru
        self.mru.next=self.lru
    
    
    def remove(self,node):
        Nodenext=Node.next
        Nodeprev=Node.prev
        
        Nodenext.prev = Nodeprev
        Nodeprev.next = Nodenext
        
        

    def get(self, key: int) -> int:
        
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
            del
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)