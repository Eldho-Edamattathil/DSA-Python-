def heapify_up(arr, i):
    while i > 0:
        parent = (i - 1) // 2
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        else:
            break

def heap_maxify(arr, i):
    l = left(i)
    r = right(i)
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap_maxify(arr, largest)
        
def heapify_down(arr, i, heap_size):
    while True:
        left_child = left(i)
        right_child = right(i)
        largest = i

        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break


# delete max valu in heap
def delete_max(arr):
    if not arr:
        return None  # Empty heap

    max_val = arr[0]
    last_element = arr.pop()
    if arr:
        arr[0] = last_element
        heapify_down(arr, 0, len(arr))

    return max_val
  
  
  
def delete_node(arr, target):
    index = arr.index(target) if target in arr else None

    if index is None:
        print(f"Node {target} not found in the heap.")
        return

    last_element = arr.pop()
    if index < len(arr):
        arr[index] = last_element
        heapify_down(arr, index, len(arr))
        heapify_up(arr, index)
        
        
        
        #///////////////////////////////////////////////////// 

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def build_heap(arr):
    n = (len(arr) // 2) - 1
    for i in range(n, -1, -1):
        heap_maxify(arr, i)

def insert_into_heap(arr, val):
    arr.append(val)
    heapify_up(arr, len(arr) - 1)
    
    
    # find kth smallest element from heap_maxify ......from heap min we can get kth largest
def delete_k_elements(arr, k):
    for _ in range(k):
        delete_max(arr)

# Example usage:
l1 = [2, 54, 6, 78, 43, 32,12,45,677,88,54,27]
build_heap(l1)
print(l1)
k=3
delete_k_elements(l1,k)
print(l1[0])
# insert_into_heap(l1, 100)
# print(l1)




# def heapify_up(arr, i):
#     while i > 0:
#         parent = (i - 1) // 2
#         if arr[i] > arr[parent]:
#             arr[i], arr[parent] = arr[parent], arr[i]
#             i = parent
#         else:
#             break

# def insert_into_heap(arr, val):
#     arr.append(val)
#     heapify_up(arr, len(arr) - 1)

# # Example usage:
# heap = []  # Initialize an empty list
# insert_into_heap(heap, 2)
# insert_into_heap(heap, 54)
# insert_into_heap(heap, 6)
# insert_into_heap(heap, 78)
# insert_into_heap(heap, 43)
# insert_into_heap(heap, 32)
# insert_into_heap(heap, 100)

# print(heap)





