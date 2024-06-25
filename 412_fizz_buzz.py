"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]

Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:

    1 <= n <= 10^4
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for idx in range(1, n+1):
            text = ""
            set_text = False
            if idx % 3 == 0:
                text += "Fizz"
                set_text = True
            if idx % 5 == 0:
                text += "Buzz"
                set_text = True
            if not set_text:
                text = str(idx)
            answer.append(text)

        return answer


if __name__ == "__main__":
    output = Solution().fizzBuzz(3)
    assert output == ["1", "2", "Fizz"]

    output = Solution().fizzBuzz(5)
    assert output == ["1", "2", "Fizz", "4", "Buzz"]

    output = Solution().fizzBuzz(15)
    assert output == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                      "FizzBuzz"]
