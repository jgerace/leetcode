"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -10^5 <= Node.val <= 10^5
"""
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        levels = defaultdict(list)
        queue = deque()
        queue.append((root, 1))
        while len(queue) > 0:
            node, level = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        max_sum = None
        min_level = None
        for level, nums in levels.items():
            total = sum(nums)
            if max_sum is None:
                max_sum = total
                min_level = level
            elif total > max_sum:
                max_sum = total
                min_level = level
        return min_level


if __name__ == "__main__":
    """tree = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    output = Solution().maxLevelSum(tree)
    assert output == 2

    tree = TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))
    output = Solution().maxLevelSum(tree)
    assert output == 2

    tree = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(0)), TreeNode(0))
    output = Solution().maxLevelSum(tree)
    assert output == 2

    tree = TreeNode(1)
    output = Solution().maxLevelSum(tree)
    assert output == 1"""

    tree = TreeNode(-1, TreeNode(-1, TreeNode(0), TreeNode(0)), TreeNode(1))
    output = Solution().maxLevelSum(tree)
    assert output == 2
