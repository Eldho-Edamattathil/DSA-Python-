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
        self.lchild.insert(data)
        
      else:
        print("NOde not found")
        
    else:
      if self.rchild:
        self.rchild.insert(data)
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
      
      
      
      
root=BST(10)
lis=[21,123,12,211,5,32]
for i in lis:
  root.insert(i)
  
root.postorder()