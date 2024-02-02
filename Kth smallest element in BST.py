# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        a = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
            

        inorder(root)
        return a[k -1]
