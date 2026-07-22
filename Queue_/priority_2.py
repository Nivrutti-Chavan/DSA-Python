from queue import PriorityQueue

# Create Priority Queue
pq = PriorityQueue()

# Insert elements (priority, value)
pq.put((3, "Task C"))
pq.put((1, "Task A"))
pq.put((2, "Task B"))

print("Priority Queue Elements:")

# Remove elements in priority order
while not pq.empty():
    priority, value = pq.get()
    print(f"Priority: {priority}, Value: {value}")