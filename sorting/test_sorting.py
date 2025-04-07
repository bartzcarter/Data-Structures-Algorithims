import unittest
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from selection_sort import selection_sort


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5,3,8,11,2,1]), [1,2,3,5,8,11])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1,2,3]), [1,2,3])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5,8,9,2,1,1]), [1,1,2,5,8,9])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1,2,3]), [1,2,3])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([5,3,8,11,2,1]), [1,2,3,5,8,11])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])

    def test_quick_sort(self):
        nums = [5,3,8,11,2,1]
        quick_sort(nums, 0, len(nums) - 1)
        self.assertEqual(nums, [1,2,3,5,8,11])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([5,3,8,11,2,1]), [1,2,3,5,8,11])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main(verbosity=2)