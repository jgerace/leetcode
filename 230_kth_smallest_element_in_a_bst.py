"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4
"""
from typing import Optional

from testing import treeNodeToBfsList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode], k: int) -> (int, int):
            if not node:
                return []

            children = dfs(node.left, k)
            children.append(node.val)
            if len(children) >= k:
                # short circuit for optimization
                return children
            children.extend(dfs(node.right, k))

            return children

        result = dfs(root, k)
        return result[k - 1]


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    output = Solution().kthSmallest(tree, 1)
    assert output == 1

    tree = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    output = Solution().kthSmallest(tree, 3)
    assert output == 3

    tree = TreeNode(5)
    output = Solution().kthSmallest(tree, 1)
    assert output == 5

    tree = TreeNode(1, None, TreeNode(2))
    output = Solution().kthSmallest(tree, 2)
    assert output == 2

    tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    output = Solution().kthSmallest(tree, 3)
    assert output == 3
