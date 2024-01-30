class TreeNode:
  def __init__(self,name,design):
    self.name=name
    self.design=design
    self.children=[]
    self.parent=None
    
  def get_level(self):
    level=0
    p=self.parent
    while p:
      level+=1
      p=p.parent
      
    return level
  
  def add_child(self,child):
    child.parent=self
    self.children.append(child)
    
  def print_tree(self,val):
    if val=="both":
      out=self.name+ '('+ self.design +')'
    elif val == "name":
      out=self.name
    else:
      out=self.design
      
    spaces=' ' * self.get_level() *3
    prefix= spaces + "|__" if self.parent else ""
    
    print(prefix + out)
    
    if self.children:
      for child in self.children:
        child.print_tree(val)
        
        
def bulid_tree():
  infra_head = TreeNode("Vishwa","Infrastructure Head")
  infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
  infra_head.add_child(TreeNode("Abhijit", "App Manager"))
  
  cto = TreeNode("Chinmay", "CTO")
  cto.add_child(infra_head)
  cto.add_child(TreeNode("Aamir", "Application Head"))
  
  hr_head = TreeNode("Gels","HR Head")
  
  hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
  hr_head.add_child(TreeNode("Waqas", "Policy Manager"))
  
  
  ceo = TreeNode("Nilupul", "CEO")
  ceo.add_child(cto)
  ceo.add_child(hr_head)
  
  
  return ceo



root_node = bulid_tree()
root_node.print_tree("name")
# # root_node.print_tree("design")
# root_node.print_tree("both")

  
  
        
        