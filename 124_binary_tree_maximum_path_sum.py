"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:

    The number of nodes in the tree is in the range [1, 3 * 10^4].
    -1000 <= Node.val <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def get_path_sum(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            left_sum = max(0, get_path_sum(node.left))
            right_sum = max(0, get_path_sum(node.right))

            max_sum = max(max_sum, left_sum + right_sum + node.val)
            return max(left_sum + node.val, right_sum + node.val)

        if not root:
            return 0

        max_sum = root.val
        path_sum = get_path_sum(root)
        return max(max_sum, path_sum)


if __name__ == "__main__":
    tree = TreeNode(-1, None, TreeNode(9, TreeNode(-6), TreeNode(3, None, TreeNode(-2))))
    output = Solution().maxPathSum(tree)
    print(output)
    assert output == 12

    tree = TreeNode(-1, TreeNode(-2, TreeNode(-6)), TreeNode(10, TreeNode(-3), TreeNode(-6)))
    output = Solution().maxPathSum(tree)
    assert output == 10

    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().maxPathSum(tree)
    assert output == 6

    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().maxPathSum(tree)
    assert output == 42

    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(-1, TreeNode(7)), TreeNode(6)))
    output = Solution().maxPathSum(tree)
    assert output == 32

    output = Solution().maxPathSum(None)
    assert output == 0
