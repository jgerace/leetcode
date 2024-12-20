"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

Constraints:

    The number of nodes in the tree is in the range [0, 1000].
    -10^9 <= Node.val <= 10^9
    -1000 <= targetSum <= 1000
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_from_node(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0

            result = 0
            if node.val == target:
                result += 1

            left_total = count_from_node(node.left, target - node.val)
            right_total = count_from_node(node.right, target - node.val)

            return left_total + right_total + result

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            from_node = count_from_node(node, targetSum)

            left_count = dfs(node.left)
            right_count = dfs(node.right)

            return from_node + left_count + right_count

        return dfs(root)


if __name__ == "__main__":
    tree = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
                    TreeNode(-3, None, TreeNode(11)))
    output = Solution().pathSum(tree, 8)
    print(output)
    assert output == 3

    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    output = Solution().pathSum(tree, 22)
    assert output == 3

    tree = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
    output = Solution().pathSum(tree, -1)
    assert output == 4

    output = Solution().pathSum(None, 3)
    assert output == 0
