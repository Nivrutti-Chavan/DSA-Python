from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        return list(self.queue)


q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

print(q.display())
print("Front:", q.front())

print("Removed:", q.dequeue())

print(q.display())