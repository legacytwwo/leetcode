class MinStack:
    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.items:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        
        self.items.append(val)
        
    def pop(self) -> None:
        if self.items[-1] == self.min[-1]:
            self.min.pop()
        self.items.pop()
        
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min[-1]

minStack = MinStack()
assert minStack.push(-1) == None
assert minStack.push(0) == None
assert minStack.push(1) == None
assert minStack.push(2) == None
assert minStack.getMin() == -1
assert minStack.pop() == None
assert minStack.getMin() == -1