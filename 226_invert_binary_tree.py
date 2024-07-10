"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from typing import Optional

from testing import treeNodeToBfsList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root


if __name__ == "__main__":
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    output = Solution().invertTree(tree)
    assert treeNodeToBfsList(output) == [4, 7, 2, 9, 6, 3, 1]

    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    output = Solution().invertTree(tree)
    assert treeNodeToBfsList(output) == [2, 3, 1]

    output = Solution().invertTree(None)
    assert output is None
