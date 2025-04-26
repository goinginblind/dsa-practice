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

    def getDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = 1 + self.getDepth(root.left)
        right_depth = 1 + self.getDepth(root.right)
        return max(left_depth, right_depth)
    
    def printTree(self, root: TreeNode = -1, prefix='', is_left=True):
        if root == -1:
            root = self.root
        if root is not None:
            print(prefix + ("└── " if is_left else "├── ") + str(root.val))
            self.printTree(root.right, prefix + ("    " if is_left else "│   "), False)
            self.printTree(root.left, prefix + ("    " if is_left else "│   "), True) 
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.fir_node = self.sec_node = None
        self.lca_current = self.lca = None
        self.p_and_q = set([p, q])

        # Traverse the tree DFS looking for nodes
        def depthFirstSearch(root, p, q):
            # If root is none or if LCA is found
            if root is None or self.lca is not None:
                return 
            # If first_node is found
            if self.fir_node is None and root in self.p_and_q:
                self.fir_node = p if root == p else (q if root == q else self.fir_node)
                return
            # If second node is found, make the highest node in the tree where we turned right the LCA
            elif self.fir_node is not None and root in self.p_and_q:
                self.sec_node = p if root == p else (q if root == q else self.sec_node)
                self.lca = self.lca_current
                return
            # Search left
            depthFirstSearch(root.left, p, q)
            # Before searching right, if it's the highest node yet and we look into right, make it a possible LCA
            if self.fir_node is not None and self.lca_current is None:
                self.lca_current = root
            depthFirstSearch(root.right, p, q)
            # If after checking everything still no second node, then possible LCA is higher up in the tree
            if self.lca_current == root:
                self.lca_current = None
            return
        
        depthFirstSearch(root, p, q)
        # If both nodes found
        if self.lca is not None:
            return self.lca
        # If only one node is found, this node is the LCA
        else:
            return self.fir_node
            


def list_to_tree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        # Attach left child
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Attach right child
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root


def main():
    null = None

    arr99 = list(range(1, 65)) 
    treeRoot, treeMap = build_bst_from_list(arr99)
    treeItself = tree(treeRoot)
    treeItself.printTree()
    print(treeItself.lowestCommonAncestor(treeRoot, treeMap[5], treeMap[40]))



main()
