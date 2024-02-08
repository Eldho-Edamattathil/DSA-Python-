def add_node(v):
  if v in graph:
    print(v,"node already present")
  else:
    graph[v]=[]
    
def add_edge(v1,v2):
  if v1 not in graph:
    print(v1, "note found")
  elif v2 not in graph:
    print(v2,"node not found")
  else:
    
    graph[v1].append(v2)
    # for directed 
    # graph[v2].append(v1)
    
    # for weighted
    # list1=[v2,val]
    # list2=[v1,val]
    # graph[v1].append(list1)
    # graph[v2].append(list2)
    
    # for direted, we need only one append
    
# def del_node(v):
#   if v not in graph:
#     print(v,"not found")
 
#   else:
#     graph.pop(v)
#     for i in graph:
#       list1=graph[i]
#       if v in list1:
#         list1.remove(v)

# for weighetd grapgh
def del_node(v):
  if v not in graph:
    print(v,"not found")
 
  else:
    graph.pop(v)
    for i in graph:
      list1=graph[i]
      for j in list1:
        if v==j[0]:
          list1.remove(j)
          break


# def del_edge(v1,v2):
#   if v1 not in graph:
#     print("not found")
#   elif v2 not in graph:
#     print("not found")
#   else:
#     # to delete edge in undirected graph, we need to go to particular key and remove node from the list of key
#     if v2 in graph[v1]:
#       graph[v1].remove(v2)
#       # for directed
#       # graph[v2].remove(v1)
#     else:
#       print("error")
 
 
    #WITH COST  
def del_edge(v1,v2,val):
  if v1 not in graph:
    print("not found")
  elif v2 not in graph:
    print("not found")
  else:
    list1=[v2,val]
    list2=[v1,val]
    if list1 in graph[v1]:
      graph[v1].remove(list1)
      graph[v1].remove(list2)
    else:
      print("error")
        
        
        # dfs recursion(stack is i=used intrnally)
def DFS(node,visited,graph):
  if node not in graph:
    print("node not present")
    return
  if node not in visited:
    print(node)
    visited.add(node)
    # if its weighted, then just add index to i, DFS(I[0],visited,graph)
    for i in graph[node]:
      DFS(i,visited,graph)


      #dfs iterative method 
def DFS_iterative(node,graph):
  visited=set()
  if node not in graph:
    print("node  not found")
    return
  stack=[]
  stack.append(node)
  while stack:
    current=stack.pop()
    if current not in visited:
      print(current)
      visited.add(current)
      for i in graph[current]:
        stack.append(i)
        
        
# bfs 
import collections
def bfs(node,graph):
  visited=set()
  if node not in graph:
    print("node not present")
    return
  queue=collections.deque([node])
  
  while queue:
    current=queue.popleft()
    visited.add(current)
    for i in graph[current]:
      if i not in visited:
        queue.append(i)
        
  print(visited)
  
  
  
    
print("before")    
graph={}
visited=set()
print("after")
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B")
add_edge("A","C")
add_edge("B","D")
add_edge("B","E")
print(graph)

# print("deleting edge")
# del_edge("A","B")
print("Travesring graph")
DFS("A",visited,graph)
print("hello")
DFS_iterative("A",graph)
print("bfs")
bfs("A",graph)
print(graph)



def bfs_shortest_distance(start_node, end_node, graph):
    visited = set()
    distance = {start_node: 0}
    
    if start_node not in graph or end_node not in graph:
        print("Start or end node not present in the graph.")
        return -1  # Indicate failure
    
    queue = collections.deque([start_node])
    
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                distance[neighbor] = distance[current] + 1
                
                if neighbor == end_node:
                    return distance[neighbor]
    
    print("End node is not reachable from the start node.")
    return -1  # Indicate failure

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start_node = 'A'
end_node = 'G'