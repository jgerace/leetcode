"""
Given a binary tree, determine if it is
height-balanced

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -10^4 <= Node.val <= 10^4
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height_of_subtree(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return max(get_height_of_subtree(node.left), get_height_of_subtree(node.right)) + 1

        if not root:
            return True

        left_height = get_height_of_subtree(root.left)
        right_height = get_height_of_subtree(root.right)
        valid_height_diff = abs(left_height - right_height) <= 1

        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)

        return is_left_balanced and is_right_balanced and valid_height_diff


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().isBalanced(tree)
    assert output is True

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    output = Solution().isBalanced(tree)
    assert output is False

    output = Solution().isBalanced(None)
    assert output is True

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    output = Solution().isBalanced(tree)
    assert output is False
