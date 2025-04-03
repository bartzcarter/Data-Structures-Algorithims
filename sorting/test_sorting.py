import unittest
from bubble_sort import bubble_sort

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([5,3,8,11,2,1]), [1,2,3,5,8,11])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1,2,3]), [1,2,3])

if __name__ == '__main__':
    unittest.main(verbosity=2)