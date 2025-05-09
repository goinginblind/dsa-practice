from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return result
        result.append(root.val)
        result += self.inorderTraversal(root.left)
        result += self.inorderTraversal(root.right)
        return result


def main():
    arr1 = [1,2,3]
    arr2 = [4,5,6]

    print(arr1 + arr2)

    arre = []
    arre += arr1

    print(arre)


main()