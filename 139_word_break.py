"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_table = {}

        def logic(input: str):
            if input in hash_table:
                return hash_table[input]
            if not input:
                return True

            for word in wordDict:
                len_word = len(word)
                print("looking at", word, len_word)
                if input.startswith(word):
                    result = logic(input[len_word:])
                    if result:
                        hash_table[input] = result
                        return result
            hash_table[input] = False
            return False

        return logic(s)


if __name__ == "__main__":
    output = Solution().wordBreak(s="leetcode", wordDict=["leet", "code"])
    assert output is True

    output = Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    assert output is True

    output = Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    assert output is False

    output = Solution().wordBreak(s="goalspecial", wordDict=["go", "goal", "goals", "special"])
    assert output is True

    output = Solution().wordBreak(
        s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
    assert output is False

    output = Solution().wordBreak(
        s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        wordDict=["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"])
    assert output is False
