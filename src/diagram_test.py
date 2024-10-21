import unittest
from diagram import draw_diagram
import numpy as np
import pandas as pd
from pathlib import Path

A = np.array([
            [ 0, -1/3, 1, 0, 1/3],
            [ 1/3, 0, 1, 0, -1/3],
            [ -1, -1, 0, 0, 1/2],
            [0, 0, 0, 0, 0],
            [-1/3, 1/3, -1/2, 0, 0]
        ])
teams=pd.DataFrame({"name": ["AB","AC","AD","BC","BD","CD"]})

class TestDiagram(unittest.TestCase):
    def test_draw_diagram(self):
        draw_diagram(teams,Path("output/sample"), A,dominated=[0])
        print("想定通りのダイアグラムだった？ y/n")
        is_desired=input()
        self.assertEqual(is_desired, "y")

if __name__ == "__main__":
    unittest.main()


