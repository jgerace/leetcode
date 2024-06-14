"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = defaultdict(int)
        sList = list(s)
        for char in sList:
            sHashMap[char] += 1

        tList = list(t)
        for char in tList:
            sHashMap[char] -= 1

        for _, value in sHashMap.items():
            if value != 0:
                return False

        return True


if __name__ == "__main__":
    output = Solution().isAnagram("anagram", "nagaram")
    assert output is True

    output = Solution().isAnagram("rat", "car")
    assert output is False

    output = Solution().isAnagram("a", "b")
    assert output is False

    output = Solution().isAnagram("a", "a")
    assert output is True
