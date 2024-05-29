"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sToT = dict()
        tToS = dict()
        sList = list(s)
        tList = list(t)
        for idx in range(len(sList)):
            sChar = sList[idx]
            tChar = tList[idx]
            sValue = sToT.get(sChar)
            tValue = tToS.get(tChar)
            if sValue is not None and tChar != sValue:
                print(sChar, "is already mapped to", sValue, "but wants to be mapped to", tChar)
                return False
            elif tValue is not None and tValue != sChar:
                print(tChar, "already mapped to", tValue, "but wants to be mapped to", sChar)
                return False
            else:
                print("hashing", sChar, "to", tChar)
                sToT[sChar] = tChar
                tToS[tChar] = sChar
        return True


if __name__ == '__main__':
    output = Solution().isIsomorphic("egg", "add")
    assert output is True

    output = Solution().isIsomorphic("foo", "bar")
    assert output is False

    output = Solution().isIsomorphic("paper", "title")
    assert output is True

    output = Solution().isIsomorphic("badc", "baba")
    assert output is False
