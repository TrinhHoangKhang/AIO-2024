class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.element = []

    def is_empty(self):
        return len(self.element) == 0

    def is_full(self):
        return len(self.element) == self.capacity

    def dequeue(self):
        if self.is_empty():
            return

        return_value = self.element[0]
        self.element.pop(0)
        return return_value

    def enqueue(self, value):
        if self.is_full():
            print('Queue is full')
            return

        self.element.append(value)

    def front(self):
        if self.is_empty():
            return
        return self.element[0]


# Test
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_full())
# >> False

print(queue1.front())
# >> 1

print(queue1.dequeue())
# >> 1

print(queue1.front())
# >> 2

print(queue1.dequeue())
# >> 2

print(queue1.is_empty())
# >> True
