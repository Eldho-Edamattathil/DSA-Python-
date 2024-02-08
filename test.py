

def max_heapify(arr,n,i):
  l=2*i+1
  r=2*i+2
  if l<n and arr[l]>arr[i]:
    largest=l
  else:
    largest=i
  if r<n and arr[r]>arr[largest]:
    largest=r
  if largest!=i:
    arr[i],arr[largest]=arr[largest],arr[i]
    max_heapify(arr,n,largest)




def bulid_heap(arr):
  n=len(arr)
  for i in range(n,-1,-1):
    max_heapify(arr,n,i)
  
  for i in range(n-1,-1,-1):
    arr[0],arr[i]=arr[i],arr[0]
    max_heapify(arr,i,0)
  
  
  
  
l1=[12, 11, 13, 5, 6, 7]
bulid_heap(l1)
print(l1)