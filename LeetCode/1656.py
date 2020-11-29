class OrderedStream:

    def __init__(self, n: int):
        self.store = dict()
        self.ptr = 1        

    def insert(self, id: int, value: str) -> List[str]:
        self.store[id] = value
        if id == self.ptr:
            if id not in self.store:
                return []
            else:
                result = []
                while self.ptr in self.store:
                    result.append(self.store[self.ptr])
                    self.ptr += 1
                return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
