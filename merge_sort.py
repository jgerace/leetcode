import math
from typing import List, Optional


def merge_sort(input: Optional[List]):
    if not input:
        return []
    if len(input) == 1:
        return input

    mid = math.floor(len(input) / 2)
    first_half = merge_sort(input[:mid])
    second_half = merge_sort(input[mid:])
    output = merge(first_half, second_half)
    return output


def merge(list1: List, list2: List) -> List:
    idx1 = 0
    idx2 = 0
    output = []

    while idx1 < len(list1) or idx2 < len(list2):
        if idx1 == len(list1):
            output.append(list2[idx2])
            idx2 += 1
            continue
        elif idx2 == len(list2):
            output.append(list1[idx1])
            idx1 += 1
            continue

        if list1[idx1] < list2[idx2]:
            output.append(list1[idx1])
            idx1 += 1
        else:
            output.append(list2[idx2])
            idx2 += 1

    return output


if __name__ == "__main__":
    output = merge_sort([2, 1])
    assert output == [1, 2]

    output = merge_sort([5, 4, 3, 2, 1])
    assert output == [1, 2, 3, 4, 5]

    output = merge_sort([5])
    assert output == [5]

    output = merge_sort([5, 4, 3, 2, 1])
    assert output == [1, 2, 3, 4, 5]
