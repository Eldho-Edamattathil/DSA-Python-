def add_node(v):
  global node_count
  if v in nodes:
    print(v,"node present")
  
  else:
    node_count+=1
    nodes.append(v)
    for i in graph:
      i.append(0)
    temp=[]
    for i in range(node_count):
      temp.append(0)
    graph.append(temp)
    
    
def add_edge(v1,v2,cost):
  if v1 not in nodes:
    print(v1, "node not present")
  elif v2 not in nodes:
    print(v2, "node not found")
  else:
    index1=nodes.index(v1)
    index2=nodes.index(v2)
    graph[index1][index2]=cost
    # if waited directed graph
    graph[index2][index1]=cost
    
def del_node(v):
  global node_count
  if v not in nodes:
    print(v,"node not found")
  else:
    index=nodes.index(v)
    node_count-=1
    nodes.remove(v)
    graph.pop(index)
    for i in graph:
      i.pop(index)

def del_edge(v1,v2):
  if v1 not in nodes:
    print(v1,"not present in nodes")
  elif v2 not in nodes:
    print(v2,"not present in nodes")
  else:
    index1=nodes.index(v1)
    index2=nodes.index(v2)
    graph[index1][index2]=0
    graph[index2][index1]=0
    
    
def print_graph():
  for i in range(node_count):
    for j in range(node_count):
      print(format(graph[i][j],"<3"), end= " ")
    print ()
      
      
nodes=[]
graph=[]
node_count=0
print("beofre adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("C","B",10)



print("after adding nodes")
print(nodes)
del_edge("A","B")

print_graph()