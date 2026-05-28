class MinStack:

    def __init__(self):
        self.stack = []
        # keep track of min values
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # stack top runs in O(1) time
        return self.minStack[-1]

        # this doesn't run O(1) time so it doesn't meet requirements
        # return min(self.stack)
