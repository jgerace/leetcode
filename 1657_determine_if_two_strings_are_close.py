"""
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

    1 <= word1.length, word2.length <= 10^5
    word1 and word2 contain only lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        print("*****")
        print("word1", word1, "word2", word2)
        # lengths need to be the same
        if len(word1) != len(word2):
            return False

        # set of letters needs to be the same
        word1_letters = defaultdict(int)
        for char in word1:
            word1_letters[char] += 1
        word1_ct_to_letters = defaultdict(set)
        for key, value in word1_letters.items():
            word1_ct_to_letters[value].add(key)
        # word1_letters = { 'a': 1, 'b': 1, 'c': 1 }
        # word1_ct_to_letters = { 1: ['a', 'b', 'c'] }

        word2_letters = defaultdict(int)
        for char in word2:
            word2_letters[char] += 1
        word2_ct_to_letters = defaultdict(set)
        for key, value in word2_letters.items():
            word2_ct_to_letters[value].add(key)

        print("  ", word1_letters, word2_letters)
        if word1_letters.keys() != word2_letters.keys():
            print("   letters not the same")
            return False
        # word2_letters = { 'a': 1, 'b': 1, 'c': 1 }
        # word2_ct_to_letters = { 1: ['a', 'b', 'c'] }

        # letter counts need to be the same even if each letter has different counts
        word1_cts = sorted(list(word1_ct_to_letters.keys()))
        word2_cts = sorted(list(word2_ct_to_letters.keys()))
        print("   word1_cts", word1_cts, "word2_cts", word2_cts)
        if len(word1_cts) != len(word2_cts):
            print("   letter counts different")
            return False

        for idx in range(len(word1_cts)):
            print("  ", word1_ct_to_letters[word1_cts[idx]], word2_ct_to_letters[word2_cts[idx]])
            if word1_cts[idx] != word2_cts[idx] or len(word1_ct_to_letters[word1_cts[idx]]) != len(word2_ct_to_letters[word2_cts[idx]]):
                return False
        return True


if __name__ == "__main__":
    output = Solution().closeStrings("abc", "bca")
    assert output is True

    output = Solution().closeStrings("a", "aa")
    assert output is False

    output = Solution().closeStrings("cabbba", "abbccc")
    assert output is True

    output = Solution().closeStrings("ca", "ab")
    assert output is False

    output = Solution().closeStrings("abbzccc", "babzzcz")
    assert output is True
