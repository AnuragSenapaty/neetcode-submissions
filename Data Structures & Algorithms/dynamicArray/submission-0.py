class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.vals = [None] * capacity


    def get(self, i: int) -> int:
        return self.vals[i]


    def set(self, i: int, n: int) -> None:
        self.vals[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.size +=1
        self.vals[self.size-1] = n

    def popback(self) -> int:
        self.size -= 1
        temp = self.vals[self.size]
        self.vals[self.size] = None
        return temp
 

    def resize(self) -> None:
        self.vals += [None]*self.cap
        self.cap *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
