class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.element = []

    def is_empty(self):
        return len(self.element) == 0

    def is_full(self):
        return len(self.element) == self.capacity

    def pop(self):
        if self.is_empty():
            return

        return_value = self.element[-1]
        self.element.pop()
        return return_value

    def push(self, value):
        if self.is_full():
            print('Stack is full')
            return

        self.element.append(value)

    def top(self):
        if self.is_empty():
            return
        return self.element[-1]


# Test
stack1 = MyStack(capacity=5)

stack1 . push(1)

stack1 . push(2)

print(stack1 . is_full())

print(stack1 . top())

print(stack1 . pop())

print(stack1 . top())

print(stack1 . pop())

print(stack1 . is_empty())
