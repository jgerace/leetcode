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

        def get_transition_genes(start: str, end: str, start_count: int) -> None:
            for idx in range(len_genes):
                if start[idx] != end[idx]:
                    temp_gene = list(start)
                    temp_gene[idx] = end[idx]
                    temp_gene = "".join(temp_gene)
                    if temp_gene in bank:
                        print("appending:", temp_gene)
                        queue.append((temp_gene, start_count))
                    else:
                        print("gene:", temp_gene, "not in bank...skipping")
            print("queue:", queue)

        get_transition_genes(startGene, endGene, 1)
        while len(queue):
            gene, counter = queue.popleft()
            print("popping:", gene, counter)
            if gene == endGene:
                return counter
            get_transition_genes(gene, endGene, counter + 1)

        return -1


if __name__ == "__main__":
    '''
    output = Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
    assert output == 1

    output = Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    assert output == 2

    output = Solution().minMutation("AACCGGTT", "AACCGGTA", [])
    assert output == -1
    '''
    output = Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])
    assert output == 4
