"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]

Constraints:

    1 <= n <= 5 * 10^4
"""
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(prefix: int):
            if prefix > n:
                return
            for idx in range(0, 10):
                candidate = prefix * 10 + idx
                if candidate <= n:
                    result.append(candidate)
                    dfs(candidate)

        for num in range(1, 10):
            if num <= n:
                result.append(num)
                dfs(num)

        print(result)
        return result


if __name__ == "__main__":
    output = Solution().lexicalOrder(13)
    assert output == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

    output = Solution().lexicalOrder(2)
    assert output == [1, 2]

    output = Solution().lexicalOrder(100)
    assert output == [1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30,
                      31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53,
                      54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76,
                      77, 78, 79, 8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
