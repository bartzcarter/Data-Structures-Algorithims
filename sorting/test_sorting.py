import unittest
from bubble_sort import bubble_sort
from merge_sort import merge_sort

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5,3,8,11,2,1]), [1,2,3,5,8,11])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1,2,3]), [1,2,3])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([5,8,9,2,1,1]), [1,1,2,5,8,9])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1,2,3]), [1,2,3])


if __name__ == '__main__':
    unittest.main(verbosity=2)