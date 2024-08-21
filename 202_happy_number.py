"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false

Constraints:

    1 <= n <= 2^31 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_digit_squares(num: int) -> int:
            sum = 0
            idx = 0
            while num > 0 and idx < 10:
                idx += 1
                digit = num % 10
                sum += digit ** 2
                num = int(num / 10)
            return sum

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_digit_squares(n)
            if n == 1:
                return True

        return False


if __name__ == "__main__":
    output = Solution().isHappy(19)
    assert output is True

    output = Solution().isHappy(2)
    assert output is False
