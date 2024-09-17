"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
"""
from collections import Counter


# TODO
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        print("*****")
        word1_hash = Counter(word1)
        word2_hash = Counter(word2)

        len_diff = abs(len(word1) - len(word2))
        num_changes = len_diff

        return num_changes


if __name__ == "__main__":
    output = Solution().minDistance(word1="horse", word2="ros")
    # assert output == 3

    output = Solution().minDistance(word1="intention", word2="execution")
    assert output == 5
