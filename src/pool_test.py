# このファイルではプールに関するテストを行う

import unittest
from pool import Pool

class TestPool(unittest.TestCase):
    def test_read_csv(self):
        # とりあえずファイルが見つかってエラー無く読み込めているか
        pool = Pool("sample.csv")
        self.assertEqual(set(pool.nodes), {"A", "B", "C", "D"})

    @unittest.skip("skip")
    def test_make_graph(self):
        pool = Pool("sample.csv")
        pool.make_graph()
        print("思った通りの図でしたか? y/n")
        answer = input()
        self.assertEqual(answer, "y")
    def test_make_matrix(self):
        pool = Pool("sample.csv")
        pool.make_matrix()
        sample_matrix = [[0,1, 1, -1 ], [-1,0 , 1, 0], [-1, -1, 0, 1], [1, 0, -1, 0]]
        self.assertEqual(pool.matrix, sample_matrix)

if __name__ == "__main__":
    unittest.main()
