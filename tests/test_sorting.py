import unittest

from src.sorting import bubble_sort, insertion_sort, selection_sort


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5, 3, 8, 6, 2]), [2, 3, 5, 6, 8])
        self.assertEqual(bubble_sort([5, 3, 8, 6, 2], reverse=True), [8, 6, 5, 3, 2])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([5, 3, 8, 6, 2]), [2, 3, 5, 6, 8])
        self.assertEqual(selection_sort([5, 3, 8, 6, 2], reverse=True), [8, 6, 5, 3, 2])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5, 3, 8, 6, 2]), [2, 3, 5, 6, 8])
        self.assertEqual(insertion_sort([5, 3, 8, 6, 2], reverse=True), [8, 6, 5, 3, 2])


if __name__ == "__main__":
    unittest.main()
