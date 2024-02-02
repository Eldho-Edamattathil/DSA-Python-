import heapq

arr=[]

heapq.heappush(arr,10)
heapq.heappush(arr,29)
heapq.heappush(arr,2)
heapq.heappush(arr,6)
print(arr)

print(heapq.heappop(arr))
print(arr)
l1=[12,4,2,3,44,32]

heapq.heapify(l1)
print(l1)

heapq.heappushpop(l1,55)
print(l1)

heapq.heapreplace(l1,120)
print(l1)

print(heapq.nlargest(2,l1))


lis=[(1,"hello"),(5,"asfsff"),(4,"sasaas")]
heapq.heapify(lis)
for i in range(len(lis)):
  print(heapq.heappop(lis))
  
