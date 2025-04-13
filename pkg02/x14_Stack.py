# 使用列表实现栈的功能
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)

s.pop()
print(s.stack)
