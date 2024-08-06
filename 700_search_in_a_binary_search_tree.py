"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:

    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 10^7
    root is a binary search tree.
    1 <= val <= 10^7
"""
from typing import Optional

from testing import treeNodeToBfsList


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == val:
            return root

        node = None
        if val < root.val:
            node = self.searchBST(root.left, val)
        elif val > root.val:
            node = self.searchBST(root.right, val)

        return node


if __name__ == "__main__":
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    output = Solution().searchBST(tree, 2)
    assert treeNodeToBfsList(output) == [2, 1, 3, None, None, None, None]

    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    output = Solution().searchBST(tree, 5)
    assert output is None

    output = Solution().searchBST(None, 5)
    assert output is None
