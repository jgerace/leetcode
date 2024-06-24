"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
among all possible results.

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

    1 <= s.length <= 10^4
    s consists of lowercase English letters.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
from collections import defaultdict


# TODO
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash_table = defaultdict(int)
        for char in list(s):
            hash_table[char] += 1

        return ""


if __name__ == "__main__":
    output = Solution().removeDuplicateLetters("bcabc")
    assert output == "abc"

    output = Solution().removeDuplicateLetters("cbacdcbc")
    assert output == "acdb"

    output = Solution().removeDuplicateLetters("b")
    assert output == "b"

    output = Solution().removeDuplicateLetters("ccbbaa")
    assert output == "abc"
