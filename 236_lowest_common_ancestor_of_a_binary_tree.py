"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

    The number of nodes in the tree is in the range [2, 10^5].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
"""
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lcaByPath(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getPath(node: Optional[TreeNode], target: int) -> Optional[deque[int]]:
            if not node:
                return None

            if node.val == target:
                path = deque()
                path.appendleft(node.val)
                return path

            leftPath = getPath(node.left, target)
            if leftPath:
                leftPath.appendleft(node.val)
                return leftPath

            rightPath = getPath(node.right, target)
            if rightPath:
                rightPath.appendleft(node.val)
                return rightPath

            # didn't find target anywhere in this subtree
            return None

        pPath = getPath(root, p.val)
        qPath = getPath(root, q.val)

        lastCommon = 0
        for idx in range(min(len(pPath), len(qPath))):
            if pPath[idx] == qPath[idx]:
                lastCommon = pPath[idx]
        return TreeNode(lastCommon)

    def lcaBySingleTraversal(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        leftLCA = self.lcaBySingleTraversal(root.left, p, q)
        rightLCA = self.lcaBySingleTraversal(root.right, p, q)

        if leftLCA and rightLCA:
            return root
        elif leftLCA:
            return leftLCA
        else:
            return rightLCA

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.lcaBySingleTraversal(root, p, q)


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))

    output = Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(1))
    assert output.val == 3

    output = Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(4))
    assert output.val == 5

    output = Solution().lowestCommonAncestor(tree, TreeNode(5), TreeNode(8))
    assert output.val == 3
