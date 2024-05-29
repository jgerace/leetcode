"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n) space
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    output = Solution().reverseWords("the sky is blue")
    assert output == "blue is sky the"

    output = Solution().reverseWords("  hello world  ")
    assert output == "world hello"

    output = Solution().reverseWords("a good   example")
    assert output == "example good a"
