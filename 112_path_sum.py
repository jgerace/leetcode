"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and targetSum - root.val == 0:
            return True

        if root.left:
            hasLeftSum = self.hasPathSum(root.left, targetSum - root.val)
            if hasLeftSum:
                return True

        if root.right:
            hasRightSum = self.hasPathSum(root.right, targetSum - root.val)
            if hasRightSum:
                return True

        return False


if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    output = Solution().hasPathSum(tree, 22)
    assert output is True

    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().hasPathSum(tree, 5)
    assert output is False

    output = Solution().hasPathSum(None, 0)
    assert output is False

    output = Solution().hasPathSum(TreeNode(1), 1)
    assert output is True
