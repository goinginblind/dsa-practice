from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        left_val = self.left.val if self.left else None
        right_val = self.right.val if self.right else None
        return f'L:{left_val}, C:{self.val}, R:{right_val}'
        
def build_bst_from_list(values):
    """Builds a BST from a level-order list (like LeetCode uses),
       and returns both the root and a dict mapping val -> TreeNode."""
    if not values:
        return None, {}

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    node_map = {root.val: root}

    while queue and index < len(values):
        node = queue.popleft()

        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
            node_map[node.left.val] = node.left
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
            node_map[node.right.val] = node.right
        index += 1

    return root, node_map



class tree:
    def __init__(self, root: TreeNode = None):
        self.root = root
    
    def printTree(self, root: TreeNode = -1, prefix='', is_left=True):
        if root == -1:
            root = self.root
        if root is not None:
            print(prefix + ("└── " if is_left else "├── ") + str(root.val))
            self.printTree(root.right, prefix + ("    " if is_left else "│   "), False)
            self.printTree(root.left, prefix + ("    " if is_left else "│   "), True) 


def main():
    null = None

    arr99 = list(range(1, 65)) 
    treeRoot, treeMap = build_bst_from_list(arr99)
    treeItself = tree(treeRoot)
    treeItself.printTree()
    print(treeItself.lowestCommonAncestor(treeRoot, treeMap[5], treeMap[40]))



main()
