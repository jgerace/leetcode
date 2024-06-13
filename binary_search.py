import math


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


if __name__ == '__main__':
    output = search([5, 25, 75], 0, 2, 75)
    assert output == 2

    output = search([5, 25, 75], 0, 2, 25)
    assert output == 1

    output = search([5, 25, 75], 0, 2, 5)
    assert output == 0

    output = search([5, 25, 75], 0, 2, 10)
    assert output == -1
