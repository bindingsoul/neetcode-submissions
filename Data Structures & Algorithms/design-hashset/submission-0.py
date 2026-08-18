class MyHashSet:

    def __init__(self):
        self.h = {}

        

    def add(self, key: int) -> None:
        self.h[key] = 0
        

    def remove(self, key: int) -> None:
        del self.h[key]        

    def contains(self, key: int) -> bool:
        if key in self.h:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)