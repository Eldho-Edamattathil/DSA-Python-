def add_node(v):
  if v in graph:
    print(v,"node already present")
  else:
    graph[v]=[]
    
def add_edge(v1,v2,val):
  if v1 not in graph:
    print(v1, "note found")
  elif v2 not in graph:
    print(v2,"node not found")
  else:
    
    graph[v1].append(v2)
    graph[v2].append(v1)
    
    # for weighted
    # list1=[v2,val]
    # list2=[v1,val]
    # graph[v1].append(list1)
    # graph[v2].append(list2)
    
    # for direted, we need only one append
    
graph={}

