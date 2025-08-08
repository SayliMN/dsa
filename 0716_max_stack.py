class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, val):
        self.stack.append(val)
        val = max(val, self.maxStack[-1] if self.maxStack else val)
        self.maxStack.append(val)

    def pop(self):
        self.stack.pop()
        self.maxStack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxStack[-1]

    def popMax(self):
        max_val = self.peekMax()
        buffer = []

        while max_val != self.top():
            buffer.append(self.stack.pop())
            self.maxStack.pop()

        self.pop()

        while buffer:
            val = buffer.pop()
            self.stack.append(val)
            new_val = max(val, self.maxStack[-1] if self.maxStack else val)
            self.maxStack.append(new_val)
        return max_val

if __name__ == "__main__":
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(5)
    s.push(8)
    s.push(4)
    print(s.top())
    print(s.popMax())
    print(s.top())
    print(s.peekMax())
    print(s.top())
    print(s.top())