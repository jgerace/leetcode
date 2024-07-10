"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val_in_path: int) -> int:
            if not node:
                return 0

            node_is_good = node.val >= max_val_in_path
            max_val_in_path = max(max_val_in_path, node.val)
            num_good_nodes_left = dfs(node.left, max_val_in_path)
            num_good_nodes_right = dfs(node.right, max_val_in_path)

            total_good_nodes = num_good_nodes_left + num_good_nodes_right
            if node_is_good:
                total_good_nodes += 1
            return total_good_nodes

        result = dfs(root, root.val)
        return result


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    output = Solution().goodNodes(tree)
    assert output == 4

    tree = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    output = Solution().goodNodes(tree)
    assert output == 3

    tree = TreeNode(1)
    output = Solution().goodNodes(tree)
    assert output == 1
