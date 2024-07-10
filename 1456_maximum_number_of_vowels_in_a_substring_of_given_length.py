"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

    1 <= s.length <= 10^5
    s consists of lowercase English letters.
    1 <= k <= s.length
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        print("*****")
        str_list = list(s)
        max_count = 0
        vowels = {"a", "e", "i", "o", "u"}
        for idx in range(k):
            if str_list[idx] in vowels:
                max_count += 1
        start, end = 1, k

        print("after initialization, max_count", max_count, "start", start, "end", end)

        current_count = max_count
        while end < len(s):
            print("looking at", str_list[start], str_list[end])
            if str_list[end] in vowels:
                print("   found end vowel")
                current_count += 1
            if str_list[start-1] in vowels:
                print("   left start vowel")
                current_count -= 1
            start += 1
            end += 1
            print("   current_count", current_count)
            max_count = max(current_count, max_count)
            print("   max_count", max_count)
            if max_count == k:
                # short circuit - we don't need to finish iterating
                break

        return max_count


if __name__ == "__main__":
    output = Solution().maxVowels("abciiidef", 3)
    assert output == 3

    output = Solution().maxVowels("aeiou", 2)
    assert output == 2

    output = Solution().maxVowels("leetcode", 3)
    assert output == 2

    output = Solution().maxVowels("l", 1)
    assert output == 0

    output = Solution().maxVowels("a", 1)
    assert output == 1
