#using heapq
import heapq
Hospital=[]

heapq.heappush(Hospital,(3,"Broken finger"))
heapq.heappush(Hospital,(1,"Heart attack"))
heapq.heappush(Hospital,(2,"High fever"))

print(heapq.heappop(Hospital))
print(heapq.heappop(Hospital))
print(heapq.heappop(Hospital))