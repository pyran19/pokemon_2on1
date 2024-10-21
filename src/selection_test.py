import unittest
from selection import selection
import numpy as np


A=np.array([
 [ 0, -1], 
 [-1, 1] 
])
B=np.array([
 [ 1, -1], 
 [-1, 1] 
])
C=np.array([
 [ 1, 0], 
 [ 0, 1] 
])
D=np.array([
 [ 1, 1], 
 [ 0, -1] 
])

class TestSelection(unittest.TestCase):
    def test_selection(self):
        self.assertAlmostEqual(selection(A), -1/3, places=4)
        self.assertAlmostEqual(selection(B), 0, places=4)
        self.assertAlmostEqual(selection(C), 1/2, places=4)
        self.assertAlmostEqual(selection(D), 1, places=4)

if __name__ == "__main__":
    unittest.main()

