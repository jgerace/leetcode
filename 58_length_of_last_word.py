"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""


class Solution:
    def lengthOfLastWordNoSplit(self, s: str) -> int:
        length = 0
        idx = len(s) - 1
        while s[idx] == ' ':
            idx -= 1
        for idx in range(idx, -1, -1):
            if s[idx] == ' ':
                return length
            length += 1
        return length

    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


if __name__ == '__main__':
    output = Solution().lengthOfLastWord("Hello World")
    assert output == 5

    output = Solution().lengthOfLastWord("   fly me   to   the moon  ")
    assert output == 4

    output = Solution().lengthOfLastWord("luffy is still joyboy")
    assert output == 6
