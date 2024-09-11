"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25



Constraints:

    -100.0 < x < 100.0
    -2^31 <= n <= 2^31-1
    n is an integer.
    Either x is not zero or n > 0.
    -10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = float(1/x)
            n *= -1
        output = 1
        if x == 1:
            return 1
        elif x == -1:
            return 1 if n % 2 == 0 else -1

        for _ in range(n):
            if abs(output) <= 0.00001:
                return 0.0
            output *= x
        print(round(output, 5))
        return round(output, 5)


if __name__ == "__main__":
    output = Solution().myPow(2.00000, 10)
    assert output == float(1024)

    output = Solution().myPow(2.10000, 3)
    assert output == float(9.261)

    output = Solution().myPow(2.00000, -2)
    assert output == 0.25000

    output = Solution().myPow(1.00000, -2147483648)
    assert output == 1.00000

    output = Solution().myPow(-1.00000, -2147483648)
    assert output == 1.00000

    output = Solution().myPow(-1.00000, -2147483647)
    assert output == -1.00000

    output = Solution().myPow(0.00001, 2147483647)
    assert output == 0

    output = Solution().myPow(2.00000, -2147483648)
    assert output == 0
