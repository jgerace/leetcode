"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        output = []

        def dfs(node, in_path, target):
            if not node:
                return

            if not node.left and not node.right and node.val - target == 0:
                # print("found root with val=", node.val)
                # print("  ", in_path, target)
                output.append(in_path + [node.val])
                return

            # print("node", node.val)
            # print("  going left", in_path + [node.val], target - node.val)
            dfs(node.left, in_path + [node.val], target - node.val)
            # print("node", node.val)
            # print("  going right", in_path + [node.val], target - node.val)
            dfs(node.right, in_path + [node.val], target - node.val)

        dfs(root, [], targetSum)

        print(output)
        return output


if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    output = Solution().pathSum(tree, targetSum=22)
    assert output == [[5, 4, 11, 2], [5, 8, 4, 5]]

    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().pathSum(tree, targetSum=5)
    assert output == []

    output = Solution().pathSum(tree, targetSum=0)
    assert output == []
