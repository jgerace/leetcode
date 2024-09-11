"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).

Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1

Constraints:

    1 <= n <= 2^31 - 1
    1 <= pick <= n

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
"""


ANSWER = 6


def guess(num: int):
    if num > ANSWER:
        return -1
    elif num < ANSWER:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        print("*****")
        start = 1
        end = n

        while start <= end:
            attempt = int((end - start)/2) + start
            ret = guess(attempt)
            print("guessed", attempt, "got", ret, "start:", start, "end:", end)
            if ret == -1:
                end = attempt - 1
            elif ret == 1:
                start = attempt + 1
            else:
                return attempt


if __name__ == "__main__":
    ANSWER = 6
    output = Solution().guessNumber(10)
    assert output == 6

    ANSWER = 1
    output = Solution().guessNumber(1)
    assert output == 1

    ANSWER = 1
    output = Solution().guessNumber(2)
    assert output == 1
