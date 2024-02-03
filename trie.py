class Trie:
  def __init__(self):
    self.root={"*":"*"}
    
  def add_word(self,word):
    cur_node=self.root
    for letter in word:
      if letter not in cur_node:
        cur_node[letter]={}
      cur_node=cur_node[letter]
    cur_node["*"]="*"
      