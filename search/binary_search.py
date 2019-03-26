from math import ceil


def binary_search(numbers: list, x: int) -> int:
    if len(numbers) == 0:
        return -1

    mid_index = ceil(len(numbers) / 2) - 1
    pivot = numbers[mid_index]

    if x == pivot:
        return x
    elif x < pivot:  # Left
        return binary_search(numbers[:mid_index], x)
    else:  # Right
        return binary_search(numbers[mid_index+1:], x)


# Tests
sorted_numbers = [1, 14, 27, 56, 57, 60, 99]
assert binary_search(sorted_numbers, 56) == 56
assert binary_search(sorted_numbers, 14) == 14
assert binary_search(sorted_numbers, 1000) == -1
