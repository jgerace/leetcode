"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

    The number of nodes in the tree is in the range [2, 10^5].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestorWithPaths(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def get_path(root: TreeNode, val: int) -> List[TreeNode]:
            path = []
            if root.val == val:
                return [root]

            if val < root.val:
                path = get_path(root.left, val)
            else:
                path = get_path(root.right, val)
            return [root] + path

        p_path = get_path(root, p.val)
        q_path = get_path(root, q.val)

        start_idx = min(len(p_path), len(q_path))
        for idx in range(start_idx, -1, -1):
            if p_path[idx].val == q_path[idx].val:
                return p_path[idx]

        return TreeNode()

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        left = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        right = None
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right


if __name__ == "__main__":
    tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    output = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(8))
    assert output.val == 6

    tree = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
    output = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(4))
    assert output.val == 2

    tree = TreeNode(2, None, TreeNode(1))
    output = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(1))
    assert output.val == 2

    tree = TreeNode(2, TreeNode(1))
    output = Solution().lowestCommonAncestor(tree, TreeNode(2), TreeNode(1))
    assert output.val == 2
