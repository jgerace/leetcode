"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
Explanation:

Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        left_branch = self.preorderTraversal(root.left)
        right_branch = self.preorderTraversal(root.right)
        return [root.val] + left_branch + right_branch

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        output = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            output.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)

        print(output)
        return output


if __name__ == "__main__":
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    output = Solution().preorderTraversal(tree)
    print(output)

    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
    output = Solution().preorderTraversal(tree)
    print(output)

    output = Solution().preorderTraversal(None)
    print(output)

    tree = TreeNode(1)
    output = Solution().preorderTraversal(tree)
    print(output)
