class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.insert(0,val)
        if(len(self.minimum) == 0):
            self.minimum.insert(0, val)
        elif (val < self.minimum[0]):
            self.minimum.insert(0,val)
        else:
            current = self.minimum[0]
            self.minimum.insert(0,current)
        
    def pop(self) -> None:
        self.stack.pop(0)
        self.minimum.pop(0)
        
    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.minimum[0]
        
        
