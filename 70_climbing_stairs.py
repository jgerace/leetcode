"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

    1 <= n <= 45
"""
from collections import defaultdict


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = defaultdict(int)
        steps[1] = 1
        steps[2] = 2
        print("*****")

        def climb(remaining: int) -> int:
            print("  remaining:", remaining)
            if remaining <= 0:
                return 0
            if steps.get(remaining):
                return steps.get(remaining)

            steps[remaining] = climb(remaining-1) + climb(remaining-2)
            return steps[remaining]

        result = climb(n)
        print("result:", result)
        return result


if __name__ == "__main__":
    output = Solution().climbStairs(2)
    assert output == 2

    output = Solution().climbStairs(3)
    assert output == 3

    output = Solution().climbStairs(6)
    assert output == 13
