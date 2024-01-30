class Treenode:
  def __init__(self,data):
    self.data=data
    self.children=[]
    self.parent=None
  
  
  def add_child(self,child):
    child.parent=self
    self.children.append(child)
    
  def get_level(self):
    level=0
    p=self.parent
    while p:
      level+=1
      p=p.parent
    return level
    
  def print_tree(self):
    spaces= ' ' * self.get_level() *3
    prefix=spaces+ "|__" if self.parent else ""
    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree()


def build_tree():
  root=Treenode("Electronics")
  
  laptop=Treenode("Laptop")
  laptop.add_child(Treenode("Lenovo"))
  laptop.add_child(Treenode("Samsung"))
  laptop.add_child(Treenode("ASUS"))
  
  mobile=Treenode("mobile")
  mobile.add_child(Treenode("Nokia"))
  mobile.add_child(Treenode("Motorola"))
  mobile.add_child(Treenode("lg"))

  tv=Treenode("TV")
  tv.add_child(Treenode("VIVO"))
  tv.add_child(Treenode("Sony"))
  
  root.add_child(laptop)
  root.add_child(mobile)
  root.add_child(tv)
  print(laptop.get_level())
  return root


root=build_tree()
root.print_tree()
  


