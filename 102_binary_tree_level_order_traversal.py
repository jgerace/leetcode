"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        class TreeNodeWithLevel:
            def __init__(self, node: TreeNode, level: int):
                self.node = node
                self.level = level

        if not root:
            return []

        queue = deque()
        queue.append(TreeNodeWithLevel(root, 0))
        levels = defaultdict(list)
        while len(queue) > 0:
            node = queue.popleft()
            levels[node.level].append(node.node.val)
            if node.node.left:
                queue.append(TreeNodeWithLevel(node.node.left, node.level+1))
            if node.node.right:
                queue.append(TreeNodeWithLevel(node.node.right, node.level+1))

        return [data for level, data in levels.items()]


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().levelOrder(tree)
    assert output == [[3], [9, 20], [15, 7]]

    tree = TreeNode(1)
    output = Solution().levelOrder(tree)
    assert output == [[1]]

    output = Solution().levelOrder(None)
    assert output == []

    tree = TreeNode(3, TreeNode(9, TreeNode(20, TreeNode(15, TreeNode(7)))))
    output = Solution().levelOrder(tree)
    assert output == [[3], [9], [20], [15], [7]]
