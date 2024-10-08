class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.temp_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.main_stack) - 1):
            self.temp_stack.append(self.main_stack.pop())
        val = self.main_stack.pop()
        while self.temp_stack:
            self.main_stack.append(self.temp_stack.pop())
            
        return val

    def peek(self) -> int:
        return self.main_stack[0]

    def empty(self) -> bool:
        return len(self.main_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()