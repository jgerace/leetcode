"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

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

from testing import treeNodeToBfsList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            left_list = []
            right_list = []
            if not node:
                return []

            if node.left:
                left_list = dfs(node.left)
            if node.right:
                right_list = dfs(node.right)
            output = left_list + [node.val] + right_list

            return output

        return dfs(root)

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        if not root:
            return []

        cur_node = root
        while True:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            elif stack:
                cur_node = stack.pop()
                output.append(cur_node.val)
                cur_node = cur_node.right
            else:
                break

        print(output)
        return output


if __name__ == "__main__":
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    output = Solution().inorderTraversal(tree)

    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, None, TreeNode(8, TreeNode(9))))
    output = Solution().inorderTraversal(tree)

    output = Solution().inorderTraversal(None)

    tree = TreeNode(1)
    output = Solution().inorderTraversal(tree)

