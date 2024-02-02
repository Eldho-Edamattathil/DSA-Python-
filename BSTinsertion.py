class BST:
  def __init__(self,key):
    self.key=key
    self.lchild=None
    self.rchild=None
    
  def insert(self,data):
    if self.key is None:
      self.key=data
      return
      
    if self.key==data:
      return
    
    if self.key>data:
      if self.lchild:
        self.lchild.insert(data)
      else:
        self.lchild=BST(data)
        
    else:
      if self.rchild:
        self.rchild.insert(data)
        
      else:
        self.rchild=BST(data)
        
  def search(self,data):
    if self.key == data:
      print("Node found")
      return
    
    if data<self.key:
      if self.lchild:
        self.lchild.search(data)
        
      else:
        print("NOde not found")
        
    else:
      if self.rchild:
        self.rchild.search(data)
      else:
        print("Node not found")
        
        
  def preorder(self):
    print(self.key)
    if self.lchild:
      self.lchild.preorder()
    if self.rchild:
      self.rchild.preorder()
      
  def postorder(self):
    
    if self.lchild:
      self.lchild.postorder()
    if self.rchild:
      self.rchild.postorder()
    print(self.key)
   
   

  def inorder(self):
    if self.lchild:
      self.lchild.inorder()
    
    print(self.key)
    if self.rchild:
      self.rchild.inorder()
      
      
  # def delete(self,data):
  #   if self.key is None:
  #     print("Tree is empty")
  #     return
  #   if data<self.key:
  #     if self.lchild:
  #       self.lchild=self.lchild.delete(data)
  #     else:
  #       print("Node not found")
  #   elif data>self.key:
  #     if self.rchild:
  #       self.rchild=self.rchild.delete(data)
  #     else:
  #       print("Node not found")
  #   else:
  #     if self.lchild is None:
  #       temp=self.rchild
  #       self=None
  #       return temp
  #     if self.rchild is None:
  #       temp=self.lchild
  #       self=None
  #       return temp
  #     node=self.rchild
  #     while node.lchild:
  #       node=node.lchild
  #     self.key=node.key
  #     self.rchild=self.rchild.delete(node.key)
  #   return self
  
  
  # delete root node
  def delete(self,data,curr):
    if self.key is None:
      print("Tree is empty")
      return
    if data<self.key:
      if self.lchild:
        self.lchild=self.lchild.delete(data,curr)
      else:
        print("Node not found")
    elif data>self.key:
      if self.rchild:
        self.rchild=self.rchild.delete(data,curr)
      else:
        print("Node not found")
    else:
      if self.lchild is None:
        temp=self.rchild
        if data==curr:
          self.key=temp.key
          self.lchild=temp.lchild
          self.rchild=temp.rchild
          temp=None
        self=None
        return temp
      if self.rchild is None:
        temp=self.lchild
        if data==curr:
          self.key=temp.key
          self.lchild=temp.lchild
          self.rchild=temp.rchild
          temp=None
        self=None
        return temp
      node=self.rchild
      while node.lchild:
        node=node.lchild
      self.key=node.key
      self.rchild=self.rchild.delete(node.key,curr)
    return self
  
  def min_node(self):
    current=self
    while current.lchild.lchild:
      current=current.lchild
    print(f'second smallest value is {current.key}')
    
  def max_node(self):
    current=self
    while current.rchild.rchild:
      current=current.rchild
    print(f'second largest value is {current.key}')
    
    
  

        
      
def count(node):
    if node is None:
      return 0
    return 1+count(node.lchild)+count(node.rchild)   
      
root=BST(10)
lis=[20,1,30,40,5]
for i in lis:
  root.insert(i)
# if count(root)>1:
  
#   root.delete(10,root.key)
# else:
#   print("Can't perform deletion")
  
root.min_node()
root.max_node()
root.inorder()