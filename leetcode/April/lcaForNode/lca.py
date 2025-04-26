from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        left_val = self.left.val if self.left else None
        right_val = self.right.val if self.right else None
        return f'L:{left_val}, C:{self.val}, R:{right_val}'


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
        self.lca = None

        # Traverse the tree DFS looking for nodes
        def depthFirstSearch(root, p, q):
            if root is None:
                return 
            if self.fir_node is None:
                self.fir_node = p if root == p else (q if root == q else self.fir_node)
                return
            elif self.sec_node is None:
                self.sec_node = p if root == p else (q if root == q else self.sec_node)
            else:
                return
            depthFirstSearch(root.left, p, q)
            if self.fir_node is not None and self.lca is not None:
                self.lca = root
            depthFirstSearch(root.right, p, q)
            self.lca = None
            return
        
        depthFirstSearch(root, p, q)
        if self.last_right_exit is not None:
            return self.last_right_exit
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

    arr99 = [3,4,5,1,2,22,23,25,null,null,null,6,9,7,13,12,11]
    root99 = list_to_tree(arr99)
    tree99 = tree(root99)
    tree99.printTree()
    print(tree.lowestCommonAncestor(root99))



main()
