"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strList = list(s)

        for char in strList:
            if char in ("(", "[", "{"):
                stack.append(char)
            else:
                try:
                    match = stack.pop()
                    if (char == ")" and match != "(" or
                        char == "]" and match != "[" or
                        char == "}" and match != "{"):
                        return False
                except IndexError:
                    # nothing in the stack
                    return False
        if len(stack) > 0:
            return False
        return True


if __name__ == '__main__':
    output = Solution().isValid("()")
    assert output is True

    output = Solution().isValid("()[]{}")
    assert output is True

    output = Solution().isValid("(]")
    assert output is False

    output = Solution().isValid("({[]})")
    assert output is True

    output = Solution().isValid("(()(())())")
    assert output is True

    output = Solution().isValid("(")
    assert output is False

    output = Solution().isValid(")")
    assert output is False
