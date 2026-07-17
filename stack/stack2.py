#use of class and object
# Stack implementation using Class and Object

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def display(self):
        return self.items[::-1]


# Creating an object
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.display())
print("Top Element:", s.peek())
print("Length:", s.length())

print("Popped Element:", s.pop())
print("Stack after pop:", s.display())

print("Is Stack Empty?", s.is_empty())