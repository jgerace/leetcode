"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10^-5 of the actual answer will be accepted.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]



Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    -2^31 <= Node.val <= 2^31 - 1
"""
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            output.append(float("{:.5f}".format(sum([val for val in nodes])/len(nodes))))
        return output


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    output = Solution().averageOfLevels(tree)
    assert output == [3.00000, 14.50000, 11.00000]

    tree = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))
    output = Solution().averageOfLevels(tree)
    assert output == [3.00000, 14.50000, 11.00000]

    tree = TreeNode(3)
    output = Solution().averageOfLevels(tree)
    assert output == [3.00000]
