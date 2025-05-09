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

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getEdges(root) -> list:
            '''Returns a list [depth_in_edges, max_diameter_alltime]'''
            if root is None:
                return [-1, 0]
            left_return, right_return = getEdges(root.left), getEdges(root.right)
            left_depth = 1 + left_return[0]
            right_depth = 1 + right_return[0]
            max_diameter = max(left_depth + right_depth, left_return[1], right_return[1])

            return [max(left_depth, right_depth), max_diameter]
        return getEdges(root)[1]
    
    def isSameTree(self, p=None, q=None) -> bool:
        def traverseTwo(root_1, root_2):
            if root_1 is None and root_2 is None:
                return True
            if (root_1 is None) != (root_2 is None):
                return False
            if root_1.val != root_2.val:
                return False
            
            if not traverseTwo(root_1.left, root_2.left) or not traverseTwo(root_1.right, root_2.right):
                return False
            else:
                return True
        
        return traverseTwo(p, q)

    def isBalanced(self, root: TreeNode) -> bool:
        self.balanced = True  # Basically assumes that the tree is balanced

        def compareDepth(root: TreeNode):
            if not self.balanced:
                return -1         # Compares each nodes left and right depths
            if root is None: 
                return 0
            left_depth = compareDepth(root.left)
            right_depth = compareDepth(root.right)
            if abs(left_depth - right_depth) > 1:  # If depth diff for L/R is more than 1
                self.balanced = False  # Tree is unbalanced
            return 1 + max(left_depth, right_depth)
        
        compareDepth(root)
        return self.balanced

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        self.subtrees = []

        def searchProbableSubtrees(root, subRoot):
            '''Appends a list of TreeNodes that could be subtrees we've been searching for 
            based on the value of two nodes, needed since numbers in the trees are not unique'''
            if root is None:
                return
            if root.val == subRoot.val:
                self.subtrees.append(root)
            searchProbableSubtrees(root.left, subRoot)
            searchProbableSubtrees(root.right, subRoot)

        def compareTwo(root_1, root_2):
            '''Checks if two trees are the same: True if same, False if not'''
            if root_1 is None and root_2 is None:
                return True
            if (root_1 is None) != (root_2 is None):
                return False
            if root_1.val != root_2.val:
                return False
            
            if not compareTwo(root_1.left, root_2.left) or not compareTwo(root_1.right, root_2.right):
                return False
            else:
                return True

        searchProbableSubtrees(root, subRoot)    
        for subtree in self.subtrees:
            if compareTwo(subtree, subRoot):
                return True
        return False
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse the tree top to bottom
        ...
        
      

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

    arr99 = [3,4,5,1,2,null,null,null,null]
    arr97 = [4,1,2]
    root99, root97 = list_to_tree(arr99), list_to_tree(arr97)
    tree99, tree97 = tree(root99), tree(root97)
    tree99.printTree()
    tree97.printTree()
    print(tree99.isSubtree(root99, root97))



main()
