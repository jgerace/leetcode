"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStrPython(self, haystack: str, needle: str) -> int:
        # Python can do this with a simple function, but I suspect that isn't the exercise here.
        # This solution is for illustrative purposes
        try:
            idx = haystack.index(needle)
            return idx
        except ValueError:
            return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # Python won't let you treat strings as lists, meaning it's not indexable without
        # first converting to a list
        haystackList = list(haystack)
        needleList = list(needle)

        haystackIdx = 0
        while haystackIdx < len(haystackList):
            if haystackList[haystackIdx] == needleList[0]:
                searchIdx = haystackIdx + 1
                needleIdx = 1
                found = True
                while needleIdx < len(needleList) and searchIdx < len(haystackList):
                    if haystackList[searchIdx] != needle[needleIdx]:
                        found = False
                        break
                    searchIdx += 1
                    needleIdx += 1
                if found:
                    return haystackIdx
                haystackIdx = searchIdx
            else:
                haystackIdx += 1
        return -1


if __name__ == '__main__':
    output = Solution().strStr("sadbutsad", "sad")
    assert output == 0

    output = Solution().strStr("leetcode", "leeto")
    assert output == -1

    output = Solution().strStr("neneedle", "needle")
    assert output == 2

    output = Solution().strStr("aaa", "aaaa")
    assert output == -1
