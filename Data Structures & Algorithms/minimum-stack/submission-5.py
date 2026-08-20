class MinStack:
    def __init__(self):
        self.stack = []
        self.prefixStack = []

    def push(self, val: int) -> None:
        if self.stack:
            if val < self.prefixStack[-1]:
                self.prefixStack.append(val)
            else:
                self.prefixStack.append(self.prefixStack[-1])
        else:
            self.prefixStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.prefixStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.prefixStack:
            return self.prefixStack[-1]
        return -1
        
