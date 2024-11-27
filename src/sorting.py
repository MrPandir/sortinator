from enum import StrEnum

__all__ = ["SortingDirection", "SortingAlgorithm", "sort_executor"]


class SortingDirection(StrEnum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"


class SortingAlgorithm(StrEnum):
    PYTHON_SORT = "Built-in Python sort"
    BUBBLE_SORT = "Bubble sort"
    SELECTION_SORT = "Selection sort"
    INSERTION_SORT = "Insertion sort"


def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        extreme_idx = i
        for j in range(i + 1, n):
            if (arr[j] < arr[extreme_idx]) ^ reverse:
                extreme_idx = j
        arr[i], arr[extreme_idx] = arr[extreme_idx], arr[i]
    return arr


def insertion_sort(arr, reverse=False):
    comparison = (lambda x, y: x < y) if not reverse else (lambda x, y: x > y)
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
        while j >= 0 and comparison(a, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = a
    return arr


FUNCTION_ALGORITHMS = {
    SortingAlgorithm.PYTHON_SORT: sorted,
    SortingAlgorithm.BUBBLE_SORT: bubble_sort,
    SortingAlgorithm.SELECTION_SORT: selection_sort,
    SortingAlgorithm.INSERTION_SORT: insertion_sort,
}


def sort_executor(
    numbers: list[int],
    algorithm: SortingAlgorithm,
    direction: SortingDirection = SortingDirection.ASCENDING,
) -> list[int]:
    """Sorts a list of integers using the specified algorithm and direction."""
    reverse = direction == SortingDirection.DESCENDING
    return FUNCTION_ALGORITHMS[algorithm](numbers, reverse=reverse)
