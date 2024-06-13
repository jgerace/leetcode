"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def flattenTree(root: Optional[TreeNode]) -> List:
            if not root:
                return []

            queue = deque()
            queue.append(root)
            output = []

            while len(queue) > 0:
                node = queue.popleft()
                if node is not None:
                    output.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    output.append(None)
            return output

        pList = flattenTree(p)
        qList = flattenTree(q)

        print("*****")
        print(pList)
        print(qList)

        return pList == qList


if __name__ == "__main__":
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    output = Solution().isSameTree(tree1, tree2)
    assert output is True

    tree1 = TreeNode(1, TreeNode(2))
    tree2 = TreeNode(1, None, TreeNode(3))
    output = Solution().isSameTree(tree1, tree2)
    assert output is False

    tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree2 = TreeNode(1, TreeNode(1), TreeNode(2))
    output = Solution().isSameTree(tree1, tree2)
    assert output is False

    output = Solution().isSameTree(None, None)
    assert output is True

    tree1 = TreeNode(1)
    tree2 = TreeNode(1)
    output = Solution().isSameTree(tree1, tree2)
    assert output is True

    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    output = Solution().isSameTree(tree1, tree2)
    assert output is False