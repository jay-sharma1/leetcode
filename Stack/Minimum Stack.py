class MinStack:
    def __init__(self):
        self.minimum = None
        self.stack = []
        self.prevMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if (self.minimum is None) or (val < self.minimum):
            self.minimum = val
        
        self.prevMin.append(self.minimum)
        

    def pop(self) -> None:
        self.stack.pop()
        self.prevMin.pop()
        if self.prevMin:
            self.minimum = self.prevMin[-1]
        else:
            self.minimum = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum