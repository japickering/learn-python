"""Implement the Quicksort algorithm

Return ``numbers`` sorted in ascending order using Quicksort.
The input list is not modified. Values equal to the pivot are kept in a
separate partition so duplicate values are handled correctly.
"""


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers.copy()

    pivot = numbers[len(numbers) // 2]
    lesser = [number for number in numbers if number < pivot]
    equal = [number for number in numbers if number == pivot]
    greater = [number for number in numbers if number > pivot]

    return quick_sort(lesser) + equal + quick_sort(greater)


# run tests
values = [83, 4, 24, 2]
print(quick_sort(values))
