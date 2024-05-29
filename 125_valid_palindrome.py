"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = list(''.join(filter(str.isalnum, s.lower())))
        print(input)
        start = 0
        end = len(input) - 1
        while start <= end:
            if input[start] != input[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    output = Solution().isPalindrome("A man, a plan, a canal: Panama")
    assert output is True

    output = Solution().isPalindrome("race a car")
    assert output is False

    output = Solution().isPalindrome(" ")
    assert output is True

    output = Solution().isPalindrome("0P")
    assert output is False
