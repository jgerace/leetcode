"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("*****")

        class Node:
            def __init__(self, val, prereqs=None):
                if prereqs is None:
                    prereqs = []
                self.val = val
                self.prereqs = prereqs.copy()

            def __repr__(self):
                return f"Node(val={self.val}, prereqs={self.prereqs}"

        node_hash = {}
        cached_results = {}

        def make_graph():
            for prereq in prerequisites:
                course_node = node_hash.get(prereq[0])
                prereq_course = prereq[1]
                """next_course_node = node_hash.get(prereq[0])
                if not next_course_node:
                    next_course_node = Node(prereq[0])
                    node_hash[prereq[0]] = next_course_node"""

                if not course_node:
                    new_course = Node(prereq[0], prereqs=[prereq_course])
                    node_hash[prereq[0]] = new_course
                else:
                    course_node.prereqs.append(prereq_course)

        def has_cycle(node: Node, seen: set) -> bool:
            print("looking at node", node)
            if not node:
                return False
            if node.val in cached_results:
                return cached_results[node.val]
            if node.val in seen:
                cached_results[node.val] = True
                return True

            seen.add(node.val)

            for prereq in node.prereqs:
                print("  analyzing prereq node", prereq)
                prereq_node = node_hash.get(prereq)
                result = has_cycle(prereq_node, seen)
                if result:
                    cached_results[node.val] = result
                    return result
            seen.remove(node.val)

            cached_results[node.val] = False
            return False

        make_graph()
        print(node_hash)

        for val, node in node_hash.items():
            print("iterating through nodes at start", val)
            seen = set()
            cycle = has_cycle(node, seen)
            if cycle:
                return False

        return True


if __name__ == "__main__":
    output = Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
    assert output is True

    output = Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
    assert output is False

    output = Solution().canFinish(numCourses=20,
                                  prerequisites=[[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1],
                                                 [17, 4]])
    assert output is False

    output = Solution().canFinish(numCourses=5, prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]])
    assert output is True

    output = Solution().canFinish(numCourses=5,
                                  prerequisites=[[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]])
    assert output is True

    output = Solution().canFinish(numCourses=100,
                                  prerequisites=[[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [4, 2], [4, 3], [5, 3], [5, 4],
                                                 [6, 4], [6, 5], [7, 5], [7, 6], [8, 6], [8, 7], [9, 7], [9, 8],
                                                 [10, 8], [10, 9], [11, 9], [11, 10], [12, 10], [12, 11], [13, 11],
                                                 [13, 12], [14, 12], [14, 13], [15, 13], [15, 14], [16, 14], [16, 15],
                                                 [17, 15], [17, 16], [18, 16], [18, 17], [19, 17], [19, 18], [20, 18],
                                                 [20, 19], [21, 19], [21, 20], [22, 20], [22, 21], [23, 21], [23, 22],
                                                 [24, 22], [24, 23], [25, 23], [25, 24], [26, 24], [26, 25], [27, 25],
                                                 [27, 26], [28, 26], [28, 27], [29, 27], [29, 28], [30, 28], [30, 29],
                                                 [31, 29], [31, 30], [32, 30], [32, 31], [33, 31], [33, 32], [34, 32],
                                                 [34, 33], [35, 33], [35, 34], [36, 34], [36, 35], [37, 35], [37, 36],
                                                 [38, 36], [38, 37], [39, 37], [39, 38], [40, 38], [40, 39], [41, 39],
                                                 [41, 40], [42, 40], [42, 41], [43, 41], [43, 42], [44, 42], [44, 43],
                                                 [45, 43], [45, 44], [46, 44], [46, 45], [47, 45], [47, 46], [48, 46],
                                                 [48, 47], [49, 47], [49, 48], [50, 48], [50, 49], [51, 49], [51, 50],
                                                 [52, 50], [52, 51], [53, 51], [53, 52], [54, 52], [54, 53], [55, 53],
                                                 [55, 54], [56, 54], [56, 55], [57, 55], [57, 56], [58, 56], [58, 57],
                                                 [59, 57], [59, 58], [60, 58], [60, 59], [61, 59], [61, 60], [62, 60],
                                                 [62, 61], [63, 61], [63, 62], [64, 62], [64, 63], [65, 63], [65, 64],
                                                 [66, 64], [66, 65], [67, 65], [67, 66], [68, 66], [68, 67], [69, 67],
                                                 [69, 68], [70, 68], [70, 69], [71, 69], [71, 70], [72, 70], [72, 71],
                                                 [73, 71], [73, 72], [74, 72], [74, 73], [75, 73], [75, 74], [76, 74],
                                                 [76, 75], [77, 75], [77, 76], [78, 76], [78, 77], [79, 77], [79, 78],
                                                 [80, 78], [80, 79], [81, 79], [81, 80], [82, 80], [82, 81], [83, 81],
                                                 [83, 82], [84, 82], [84, 83], [85, 83], [85, 84], [86, 84], [86, 85],
                                                 [87, 85], [87, 86], [88, 86], [88, 87], [89, 87], [89, 88], [90, 88],
                                                 [90, 89], [91, 89], [91, 90], [92, 90], [92, 91], [93, 91], [93, 92],
                                                 [94, 92], [94, 93], [95, 93], [95, 94], [96, 94], [96, 95], [97, 95],
                                                 [97, 96], [98, 96], [98, 97], [99, 97]])
    assert output is True
