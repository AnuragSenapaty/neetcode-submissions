class LinkedList:
    
    def __init__(self):
        self.vals = []
    
    def get(self, index: int) -> int:
        try:
            return self.vals[index]
        except:
            return -1

    def insertHead(self, val: int) -> None:
        self.vals = [val] + self.vals

    def insertTail(self, val: int) -> None:
        self.vals.append(val)

    def remove(self, index: int) -> bool:
        try:
            self.vals.pop(index)
            return True
        except:
            return False

    def getValues(self) -> List[int]:
        return self.vals
