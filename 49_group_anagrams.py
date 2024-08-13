"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List

from testing import listItemsEqual


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            word_map[sorted_word].append(word)

        print([value for value in word_map.values()])
        return [value for value in word_map.values()]


if __name__ == "__main__":
    output = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert listItemsEqual(output, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])

    output = Solution().groupAnagrams([""])
    assert output == [[""]]

    output = Solution().groupAnagrams(["a"])
    assert output == [["a"]]
