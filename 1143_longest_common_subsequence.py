"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        print("*****", text1, text2)
        len_1 = len(text1)
        len_2 = len(text2)

        # TODO: For some reason this works but the first way of expressing the matrix does not...
        # dp = [[0] * (len_2+1)] * (len_1+1)
        dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

        for idx1 in range(1, len_1+1):
            for idx2 in range(1, len_2+1):
                print(dp, idx1, idx2)

                if text1[idx1-1] == text2[idx2-1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + 1
                else:
                    dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])

        print(dp)

        return dp[-1][-1]


if __name__ == "__main__":
    output = Solution().longestCommonSubsequence(text1="abcde", text2="ace")
    assert output == 3

    output = Solution().longestCommonSubsequence(text1="abc", text2="abc")
    assert output == 3

    output = Solution().longestCommonSubsequence(text1="abc", text2="def")
    assert output == 0

    output = Solution().longestCommonSubsequence(text1="ezupkr", text2="ubmrapg")
    assert output == 2

    output = Solution().longestCommonSubsequence(text1="bsbininm", text2="jmjkbkjkv")
    assert output == 1

    output = Solution().longestCommonSubsequence(text1="abcba", text2="abcbcba")
    assert output == 5
