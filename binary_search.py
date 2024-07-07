import bisect
import math
from typing import List


def search(numbers, start, end, target) -> int:
    if end < start:
        return -1
    idx = math.floor((end + start) / 2)
    if numbers[idx] == target:
        return idx

    if target > numbers[idx]:
        return search(numbers, idx + 1, end, target)
    else:
        return search(numbers, start, idx - 1, target)


def bisect_left(target: int, numbers: List[int]) -> int:
    print("*****")
    print(target, numbers)
    # finds index in numbers where target would be inserted such that everything right of
    # idx is >= target and everything left is < target
    start = 0
    end = len(numbers) - 1

    if target < numbers[0]:
        return 0
    elif target > numbers[len(numbers)-1]:
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
    print("returning start", start)
    return start


if __name__ == '__main__':
    output = search([5, 25, 75], 0, 2, 75)
    assert output == 2

    output = search([5, 25, 75], 0, 2, 25)
    assert output == 1

    output = search([5, 25, 75], 0, 2, 5)
    assert output == 0

    output = search([5, 25, 75], 0, 2, 10)
    assert output == -1

    output = bisect_left(3, [1, 3, 5])
    assert output == 1
    assert output == bisect.bisect_left([1, 3, 5], 3)

    output = bisect_left(0, [1, 3, 5])
    assert output == 0
    assert output == bisect.bisect_left([1, 3, 5], 0)

    output = bisect_left(3, [1, 2, 3, 4])
    assert output == 2
    assert output == bisect.bisect_left([1, 2, 3, 4], 3)

    output = bisect_left(3, [1, 2, 4, 5])
    assert output == 2
    assert output == bisect.bisect_left([1, 2, 4, 5], 3)

    output = bisect_left(36, [22, 22, 29, 35, 37, 40])
    assert output == 4
    assert output == bisect.bisect_left([22, 22, 29, 35, 37, 40], 36)

    output = bisect_left(8, [5, 8, 8])
    assert output == 1
    assert output == bisect.bisect_left([5, 8, 8], 8)
