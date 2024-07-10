"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left
    subtree
    of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst_with_boundary(node: Optional[TreeNode], min: Optional[int], max: Optional[int]) -> bool:
            if not node:
                print("null node")
                return True

            print("node", node.val, "min", min, "max", max)

            if min is not None and node.val <= min:
                print("fail min test")
                return False
            elif max is not None and node.val >= max:
                print("fail max test")
                return False

            print("left subtree")
            left_valid = is_bst_with_boundary(node.left, min, node.val)
            print("right subtree")
            right_valid = is_bst_with_boundary(node.right, node.val, max)

            return left_valid and right_valid

        print("*****")
        return is_bst_with_boundary(root, None, None)


if __name__ == "__main__":
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    output = Solution().isValidBST(tree)
    assert output is True

    tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    output = Solution().isValidBST(tree)
    assert output is False

    output = Solution().isValidBST(None)
    assert output is True

    tree = TreeNode(2)
    output = Solution().isValidBST(tree)
    assert output is True

    tree = TreeNode(2, TreeNode(1, TreeNode(0)))
    output = Solution().isValidBST(tree)
    assert output is True

    tree = TreeNode(2, TreeNode(2), TreeNode(2))
    output = Solution().isValidBST(tree)
    assert output is False

    tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    output = Solution().isValidBST(tree)
    assert output is False

    tree = TreeNode(0, None, TreeNode(-1))
    output = Solution().isValidBST(tree)
    assert output is False

    tree = TreeNode(32, TreeNode(26, TreeNode(19, None, TreeNode(27))), TreeNode(47, None, TreeNode(56)))
    output = Solution().isValidBST(tree)
    assert output is False
