"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:

    1 <= s.length <= 10^5
    s[i] is either 'A', 'C', 'G', or 'T'.
"""
from collections import defaultdict
from typing import List

from testing import listItemsEqual


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        len_str = len(s)
        counts = defaultdict(int)

        if len_str < 10:
            return []

        start = 0
        end = 10
        while end <= len_str:
            counts[s[start:end]] += 1
            start += 1
            end += 1

        return [seq for seq, count in counts.items() if count > 1]


if __name__ == "__main__":
    output = Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    assert listItemsEqual(output, ["AAAAACCCCC", "CCCCCAAAAA"])

    output = Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")
    assert listItemsEqual(output, ["AAAAAAAAAA"])

    output = Solution().findRepeatedDnaSequences("A")
    assert listItemsEqual(output, [])
