"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def get_leaf_nodes(root: Optional[TreeNode], leaves: List[int]):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)
                return

            if root.left:
                get_leaf_nodes(root.left, leaves)
            if root.right:
                get_leaf_nodes(root.right, leaves)

        tree1_leaves = []
        get_leaf_nodes(root1, tree1_leaves)

        tree2_leaves = []
        get_leaf_nodes(root2, tree2_leaves)

        if len(tree1_leaves) != len(tree2_leaves):
            return False
        else:
            for idx in range(len(tree1_leaves)):
                if tree1_leaves[idx] != tree2_leaves[idx]:
                    return False

        return True


if __name__ == "__main__":
    tree1 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(9), TreeNode(8)))
    tree2 = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))))
    output = Solution().leafSimilar(tree1, tree2)
    assert output is True

    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(3), TreeNode(2))
    output = Solution().leafSimilar(tree1, tree2)
    assert output is False

    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    output = Solution().leafSimilar(tree1, tree2)
    assert output is True

    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    output = Solution().leafSimilar(tree1, tree2)
    assert output is False
