"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8
"""
from typing import List

from testing import listItemsEqual


class Solution:

    # Complexity: O(2^N)
    def generateParenthesis(self, n: int) -> List[str]:
        def getParens(input: str, lefts: int, rights: int) -> List[str]:
            if lefts == 0 and rights == 0:
                return [input]

            output = []
            if lefts > 0:
                left_parens = getParens(input + "(", lefts - 1, rights)
                output.extend(left_parens)
            if rights > lefts:
                right_parens = getParens(input + ")", lefts, rights - 1)
                output.extend(right_parens)
            return output

        output = getParens("", n, n)
        return output


if __name__ == "__main__":
    output = Solution().generateParenthesis(2)
    assert listItemsEqual(output, ["()()", "(())"])

    output = Solution().generateParenthesis(3)
    assert listItemsEqual(output, ["((()))", "(()())", "(())()", "()(())", "()()()"])

    output = Solution().generateParenthesis(1)
    assert listItemsEqual(output, ["()"])

    output = Solution().generateParenthesis(4)
    assert listItemsEqual(output,
                          ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
                           "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
