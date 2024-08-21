"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

    For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

    0 <= bank.length <= 10
    startGene.length == endGene.length == bank[i].length == 8
    startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        print("*****")
        print("start:", startGene, "end:", endGene)
        queue = deque()
        len_genes = 8

        queue.append((startGene, 0))
        used = set()
        while len(queue):
            cur_gene, counter = queue.popleft()
            print("popping:", cur_gene, counter)
            if cur_gene == endGene:
                print("  match:", counter)
                return counter
            for gene in bank:
                if gene in used:
                    continue
                print("  comparing to", gene)
                diff_ct = 0
                for idx in range(len_genes):
                    if cur_gene[idx] != gene[idx]:
                        diff_ct += 1
                if diff_ct == 1:
                    print("  queueing:", gene, counter + 1)
                    queue.append((gene, counter + 1))
                    used.add(gene)
                else:
                    print("  too many diffs:", diff_ct)

        print("no match")
        return -1


if __name__ == "__main__":

    output = Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
    assert output == 1

    output = Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    assert output == 2

    output = Solution().minMutation("AACCGGTT", "AACCGGTA", [])
    assert output == -1

    output = Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])
    assert output == 4
