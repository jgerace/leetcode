"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

    The number of nodes in the tree is in the range [0, 10^4].
    -100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = max(self.maxDepth(root.left), self.maxDepth(root.right))

        return maxDepth + 1


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().maxDepth(tree)
    assert output == 3

    tree = TreeNode(1, None, TreeNode(2))
    output = Solution().maxDepth(tree)
    assert output == 2

    tree = TreeNode(1, TreeNode(2), None)
    output = Solution().maxDepth(tree)
    assert output == 2

    output = Solution().maxDepth(None)
    assert output == 0
