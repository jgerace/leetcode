"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)

        idx1 = 0
        idx2 = 0
        result = ""
        while idx1 + idx2 < len_word1 + len_word2:
            if idx1 < len_word1:
                result += word1[idx1]
                idx1 += 1
            if idx2 < len_word2:
                result += word2[idx2]
                idx2 += 1

        return result


if __name__ == "__main__":
    output = Solution().mergeAlternately("abc", "pqr")
    assert output == "apbqcr"

    output = Solution().mergeAlternately("ab", "pqrs")
    assert output == "apbqrs"

    output = Solution().mergeAlternately("abcd", "pq")
    assert output == "apbqcd"
