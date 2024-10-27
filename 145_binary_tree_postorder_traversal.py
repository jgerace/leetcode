"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]

Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]

Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        print("*****")

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            result.append(node.val)

        dfs(root)
        return result

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = deque()

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            result.appendleft(node.val)

        return list(result)


if __name__ == "__main__":
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    output = Solution().postorderTraversal(tree)
    # assert output == [3, 2, 1]
    print(output)

    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
                    TreeNode(3, None, TreeNode(8, TreeNode(9))))
    output = Solution().postorderTraversal(tree)
    # assert output == [4, 6, 7, 5, 2, 9, 8, 3, 1]
    print(output)

    output = Solution().postorderTraversal(None)
    print(output)

    tree = TreeNode(1)
    output = Solution().postorderTraversal(tree)
    print(output)

