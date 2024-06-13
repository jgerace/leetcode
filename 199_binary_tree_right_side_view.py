"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        class TreeNodeWithLevel:
            def __init__(self, treeNode, level):
                self.node = treeNode
                self.level = level

        levels = defaultdict(list)
        queue = deque()
        rootNodeWithLevel = TreeNodeWithLevel(root, 0)
        queue.append(rootNodeWithLevel)

        while len(queue) > 0:
            node = queue.popleft()
            levels[node.level].append(node.node.val)
            if node.node.left:
                queue.append(TreeNodeWithLevel(node.node.left, node.level+1))
            if node.node.right:
                queue.append(TreeNodeWithLevel(node.node.right, node.level+1))

        output = []
        for level, nodes in levels.items():
            output.append(nodes[len(nodes)-1])
        return output


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    output = Solution().rightSideView(tree)
    assert output == [1, 3, 4]

    tree = TreeNode(1, None, TreeNode(3))
    output = Solution().rightSideView(tree)
    assert output == [1, 3]

    output = Solution().rightSideView(None)
    assert output == []
