"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        minLen = min([len(s) for s in strs])

        for idx in range(minLen):
            prefix += strs[0][idx]
            for s in strs:
                if s[idx] != prefix[idx]:
                    return prefix[:-1]

        return prefix


if __name__ == '__main__':
    output = Solution().longestCommonPrefix(["flower", "flow", "flight"])
    assert output == "fl"

    output = Solution().longestCommonPrefix(["dog", "racecar", "car"])
    assert output == ""

    output = Solution().longestCommonPrefix(["dog", "dog", "dog"])
    assert output == "dog"
