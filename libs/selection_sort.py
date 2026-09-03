"""
Implement the selection sort algorithm
Sort ``numbers`` in ascending order using selection sort
The list is sorted in place and returned for convenient use
by callers
"""


def selection_sort(numbers):
    for index in range(len(numbers) - 1):
        minimum_index = index

        for candidate_index in range(index + 1, len(numbers)):
            if numbers[candidate_index] < numbers[minimum_index]:
                minimum_index = candidate_index

        if minimum_index != index:
            numbers[index], numbers[minimum_index] = (
                numbers[minimum_index],
                numbers[index],
            )

    return numbers
