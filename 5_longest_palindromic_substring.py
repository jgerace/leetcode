"""
Given a string s, return the longest
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        print("*****")

        max_start = 0
        max_end = 0
        for idx in range(len(s)):
            left = idx
            right = idx
            # accounts for odd-number length palindromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > max_end - max_start:
                max_start = left + 1
                max_end = right - 1

            left = idx
            right = idx + 1
            # accounts for even-number length palindromes
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > max_end - max_start:
                max_start = left + 1
                max_end = right - 1

        print("result:", s[max_start:max_end+1])
        return s[max_start:max_end+1]


if __name__ == "__main__":
    output = Solution().longestPalindrome("babad")
    assert output == "bab" or output == "aba"

    output = Solution().longestPalindrome("cbbd")
    assert output == "bb"

    output = Solution().longestPalindrome("dcbbcd")
    assert output == "dcbbcd"

    output = Solution().longestPalindrome("dcbcd")
    assert output == "dcbcd"

    output = Solution().longestPalindrome("a")
    assert output == "a"

    output = Solution().longestPalindrome("babaddtattarrattatddetartrateedredividerb")
    assert output == "ddtattarrattatdd"

