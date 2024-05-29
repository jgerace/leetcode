"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]
        for child in range(1, len(ratings)):
            candies.append(1)
            if ratings[child] < ratings[child - 1]:
                candies[child - 1] += 1
            elif ratings[child] > ratings[child - 1]:
                candies[child] += candies[child - 1]
            elif child < len(ratings)-1 and ratings[child] > ratings[child + 1]:
                candies[child] += 1
        return sum(candies)


if __name__ == '__main__':
    output = Solution().candy([1, 0, 2])
    assert output == 5

    output = Solution().candy([1, 2, 2])
    assert output == 4

    output = Solution().candy([1])
    assert output == 1

    output = Solution().candy([1, 2, 5, 5, 5, 2, 1])
    assert output == 13
