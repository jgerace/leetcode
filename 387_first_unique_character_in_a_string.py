"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

Constraints:

    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
"""
from collections import Counter, defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for idx, char in enumerate(s):
            if counts[char] == 1:
                return idx

        return -1


if __name__ == "__main__":
    output = Solution().firstUniqChar("leetcode")
    assert output == 0

    output = Solution().firstUniqChar("loveleetcode")
    assert output == 2

    output = Solution().firstUniqChar("aabb")
    assert output == -1
