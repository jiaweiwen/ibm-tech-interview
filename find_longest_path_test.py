'''This script verifies the correctness of the function LongestSequence in
find_longest_path.py

To run the unittest in command: $python -m find_longest_path_test
'''

import unittest
from find_longest_path_single import LongestSequence

class TestFindLongestPath(unittest.TestCase):

	def test_longest_sequence(self):
		target_grid = []
		self.assertEqual(LongestSequence(target_grid, 0, 0, [], []), 
						 [])

		target_grid = [[1, 6, 5], [2, 3, 4], [9, 4, 5]]
		self.assertEqual(LongestSequence(target_grid, 0, 0, [], []), 
						 [1, 2, 3, 4, 5, 6])

		target_grid = [[1, 2, 3], [2, 3, 4], [9, 6, 5]]
		self.assertEqual(LongestSequence(target_grid, 0, 0, [], []), 
						 [1, 2, 3, 4, 5, 6])

		target_grid = [[1, 6, 7], [3, 5, 8], [5, 4, 5]]
		self.assertEqual(LongestSequence(target_grid, 0, 0, [], []), 
						 [1])
		

if __name__ == '__main__':
    unittest.main()
