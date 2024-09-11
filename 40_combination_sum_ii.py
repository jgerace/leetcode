"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""
from typing import List

from testing import listItemsEqual


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print("*****")
        result = []

        def backtrack(idx_cand: int, tgt: int, cur_comb: List[int]) -> None:
            if tgt == 0:
                result.append(cur_comb)
                return
            for idx in range(idx_cand, len(candidates)):
                if idx > idx_cand and candidates[idx] == candidates[idx-1]:
                    # ignore duplicates
                    continue
                if candidates[idx] > tgt:
                    return
                # making a copy of cur_comb + new candidate instead of appending means we don't have
                # to pop when backtrack returns
                # moreover, when i append cur_comb to result, i would also have to make a copy THERE instead
                # so this solution saves a couple lines of code
                backtrack(idx + 1, tgt - candidates[idx], cur_comb + [candidates[idx]])

        backtrack(0, target, [])
        print(result)
        return result


if __name__ == "__main__":
    output = Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
    assert listItemsEqual(output, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])

    output = Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5)
    assert output == [[1, 2, 2], [5]]

    output = Solution().combinationSum2(candidates=[3, 1, 3, 5, 1, 1], target=8)
    assert output == [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]

    output = Solution().combinationSum2(
        candidates=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=27)
    assert output == []

    output = Solution().combinationSum2(
        candidates=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1], target=30)
    assert output == [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
