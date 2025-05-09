from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr.left:
            curr = curr.left
        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minimum_value = self.getMinNode(root.right).val
                root.val = minimum_value
                root.right = self.deleteNode(root.right, minimum_value)
        
        return root