"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def traverse(root: TreeNode, num: int, total: int) -> int:
            num *= 10
            num += root.val

            if not root.left and not root.right:
                return total + num

            if root.left:
                total = traverse(root.left, num, total)
            if root.right:
                total = traverse(root.right, num, total)

            return total

        total = traverse(root, 0, 0)

        return total


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().sumNumbers(tree)
    assert output == 25

    tree = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    output = Solution().sumNumbers(tree)
    assert output == 1026

    tree = TreeNode(1, None, TreeNode(3, None, TreeNode(2)))
    output = Solution().sumNumbers(tree)
    assert output == 132

    tree = TreeNode(1, TreeNode(2, TreeNode(3)))
    output = Solution().sumNumbers(tree)
    assert output == 123

    tree = TreeNode(1)
    output = Solution().sumNumbers(tree)
    assert output == 1
