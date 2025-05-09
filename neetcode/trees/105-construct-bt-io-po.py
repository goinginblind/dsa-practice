from typing import Dict, Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inorder  = [1,0,2,4,3,7,11,8,13]
# preorder = [3,4,0,1,2,7,13,11,8]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: index for index, val in enumerate(inorder)}
        preorder_index = 0

        def linkNodes(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            # Get the current root from preorder
            root_value = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(val=root_value)

            # Get index of root in inorder
            index_in_inorder = inorder_map[root_value]

            # Build left and right subtrees
            root.left = linkNodes(left, index_in_inorder - 1)
            root.right = linkNodes(index_in_inorder + 1, right)

        return linkNodes(0, len(inorder) - 1)
