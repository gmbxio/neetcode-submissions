class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashTable = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for item in self.hashTable[index]:
            if item[0] == key:
                item[1] = value
                return
        self.hashTable[index].append([key, value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        for item in self.hashTable[index]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for item in self.hashTable[index]:
            if item[0] == key:
                self.hashTable.pop(index)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)