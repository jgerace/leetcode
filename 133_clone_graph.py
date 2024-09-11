"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.

Constraints:

    The number of nodes in the graph is in the range [0, 100].
    1 <= Node.val <= 100
    Node.val is unique for each node.
    There are no repeated edges and no self-loops in the graph.
    The Graph is connected and all nodes can be visited starting from the given node.
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = {}
        queue = deque()
        queue.append(node)
        new_nodes = {}

        while len(queue):
            cur_node = queue.popleft()

            # seen means i've added all neighbors
            seen[cur_node.val] = cur_node

            # create the new node
            new_cur = new_nodes.get(cur_node.val)
            if not new_cur:
                new_cur = Node(cur_node.val)
                new_nodes[new_cur.val] = new_cur

            # add one-way relationship from new node to neighbors
            for node in cur_node.neighbors:
                if not seen.get(node.val):
                    queue.append(node)

                new_neighbor = new_nodes.get(node.val)
                if not new_neighbor:
                    new = Node(val=node.val)
                    new_cur.neighbors.append(new)
                    new_nodes[new.val] = new
                else:
                    if new_neighbor not in new_cur.neighbors:
                        new_cur.neighbors.append(new_neighbor)

        return new_nodes[1]


if __name__ == "__main__":
    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3)
    node4 = Node(val=4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    output = Solution().cloneGraph(node1)
