#importing dequeue
from collections import deque

queue=deque()
#Adding element
queue.append("A")
queue.append("B")
queue.append("C")

#removing element from 0th index
first=queue.popleft()

#to viewing top element
view=queue[0]

#to see is empty(False means element present)
empty=len(queue)==0

#length of queue
length=len(queue)
