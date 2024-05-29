"""
Given a string s, find the length of the longest
substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strList = list(s)

        seen = defaultdict(lambda: -1)  # index of last iteration of this letter
        maxLen = 0
        curLen = 0
        idx = 0
        while idx < len(strList):
            char = strList[idx]
            if seen[char] == -1:
                seen[char] = idx
                curLen += 1
                idx += 1
                continue

            maxLen = max(curLen, maxLen)
            idx = seen[char] + 1
            seen.clear()
            curLen = 0

        maxLen = max(curLen, maxLen)
        return maxLen


if __name__ == '__main__':
    output = Solution().lengthOfLongestSubstring("abcabcbb")
    assert output == 3

    output = Solution().lengthOfLongestSubstring("bbbbb")
    assert output == 1

    output = Solution().lengthOfLongestSubstring("pwwkew")
    assert output == 3

    output = Solution().lengthOfLongestSubstring("p")
    assert output == 1

    output = Solution().lengthOfLongestSubstring("dvdf")
    assert output == 3
