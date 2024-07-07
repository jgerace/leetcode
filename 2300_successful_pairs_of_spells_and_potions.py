"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
Thus, [2,0,2] is returned.

Constraints:

    n == spells.length
    m == potions.length
    1 <= n, m <= 10^5
    1 <= spells[i], potions[i] <= 10^5
    1 <= success <= 10^10
"""
import bisect
import math
from typing import List

from testing import listItemsEqual


class Solution:
    @staticmethod
    def search_for_target_or_min(target: int, numbers: List[int]) -> int:
         # TODO: Haven't been able to get this to work...
        print("searching for", target, "in", numbers)
        # returns the index of target or the index of the minimum number in numbers
        # bigger than target
        start = 0
        end = len(numbers) - 1

        if target < numbers[0]:
            return 0
        elif target > numbers[len(numbers) - 1]:
            return -1

        while end > start:
            if target == numbers[start]:
                return start

            idx = (end + start) // 2
            print("start", start, "end", end, "idx", idx)
            if target == numbers[idx]:
                print("found target at", idx)
                return idx
            if target > numbers[idx]:
                print("looking right")
                start = idx + 1
            else:
                print("looking left")
                end = idx
        return start

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        print("*****")
        potions.sort()
        result = []
        num_potions = len(potions)
        for spell_power in spells:
            minimum_potion_power = math.ceil(success / spell_power)
            # search for the potions with this power in the sorted potion list
            idx = self.search_for_target_or_min(minimum_potion_power, potions)
            # idx = bisect.bisect_left(potions, minimum_potion_power)
            print("num potions", num_potions, "idx", idx)

            # this and everything more powerful is the result (num_potions - search index)
            if idx < 0:
                result.append(0)
            else:
                result.append(num_potions - idx)
        print(result)
        return result


if __name__ == "__main__":
    output = Solution.search_for_target_or_min(3, [1, 3, 5])
    assert output == 1

    output = Solution.search_for_target_or_min(0, [1, 3, 5])
    assert output == 0

    output = Solution.search_for_target_or_min(3, [1, 2, 3, 4])
    assert output == 2

    output = Solution.search_for_target_or_min(3, [1, 2, 4, 5])
    assert output == 2

    output = Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
    assert listItemsEqual(output, [4, 0, 3])

    output = Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)
    assert listItemsEqual(output, [2, 0, 2])

    output = Solution().successfulPairs([15, 8, 19], [38, 36, 23], 328)
    assert listItemsEqual(output, [3, 0, 3])

    output = Solution().successfulPairs([9, 39], [35, 40, 22, 37, 29, 22], 320)
    assert listItemsEqual(output, [2, 6])
