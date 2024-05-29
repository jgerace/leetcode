"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for letter in list(magazine):
            letters[letter] += 1

        for letter in list(ransomNote):
            if letters[letter] == 0:
                return False
            letters[letter] -= 1
        return True

if __name__ == '__main__':
    output = Solution().canConstruct("a", "b")
    assert output is False

    output = Solution().canConstruct("aa", "ab")
    assert output is False

    output = Solution().canConstruct("aa", "aab")
    assert output is True
