"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

Constraints:

    0 <= s.length <= 3 * 10^4
    s[i] is '(', or ')'.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        valid_idxs = [0] * len(s)
        for idx, char in enumerate(list(s)):
            if char == ")":
                if len(stack):
                    prev_idx, char = stack.pop()
                    valid_idxs[idx] = 1
                    valid_idxs[prev_idx] = 1
            else:
                stack.append((idx, char))

        max_len = 0
        cur_len = 0
        for val in valid_idxs:
            if val:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0

        return max_len


if __name__ == "__main__":
    output = Solution().longestValidParentheses("(()")
    assert output == 2

    output = Solution().longestValidParentheses(")()())")
    assert output == 4

    output = Solution().longestValidParentheses("")
    assert output == 0

    output = Solution().longestValidParentheses("()(()")
    assert output == 2
