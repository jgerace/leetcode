"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""
from typing import List, Optional

from collections import defaultdict, deque
from testing import listItemsEqual


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        print("*****")
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        levels = defaultdict(list)
        max_level = 0
        while len(queue):
            node, level = queue.popleft()
            levels[level].append(node.val)
            if level > max_level:
                max_level = level

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        result = []
        for level in range(max_level, -1, -1):
            result.append(levels[level])
        print(result)
        return result


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().levelOrderBottom(tree)
    assert listItemsEqual(output, [[15, 7], [9, 20], [3]])

    tree = TreeNode(1)
    output = Solution().levelOrderBottom(tree)
    assert listItemsEqual(output, [[1]])

    output = Solution().levelOrderBottom(None)
    assert output == []
