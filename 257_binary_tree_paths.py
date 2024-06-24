"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]

Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []

        def traverse(root, input) -> None:
            level_input = input + f"{root.val}"
            if not root.left and not root.right:
                output.append(level_input)
                return

            if root.left:
                traverse(root.left, level_input + "->")
            if root.right:
                traverse(root.right, level_input + "->")

        traverse(root, f"")
        return output


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    output = Solution().binaryTreePaths(tree)
    assert output == ["1->2->5", "1->3"]

    tree = TreeNode(1)
    output = Solution().binaryTreePaths(tree)
    assert output == ["1"]
