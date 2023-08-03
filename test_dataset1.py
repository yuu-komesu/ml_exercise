from dataset1 import true_function
import unittest
import numpy as np

class TestFunctionMethods1(unittest.TestCase):
	def test_zero(self):
		x=np.linspace(0, 0, 1)
		self.assertEqual(true_function(x), np.zeros((1,), dtype=float))
	
	def test_two_zeros(self):
		x=np.linspace(0, 0, 2)
		arr1=true_function(x)
		arr2=np.zeros((2,), dtype=float)
		self.assertEqual(list(arr1), list(arr2))

if __name__ == '__main__':
	unittest.main()
