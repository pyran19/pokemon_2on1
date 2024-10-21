import unittest
from matching import Matching
from pool import Pool
from numpy.testing import assert_allclose

class TestMatching(unittest.TestCase):
    def test_matching(self):
        pool = Pool("sample.csv")
        matching = Matching(pool)
        sample_relations = [
            [0, 0, -1/2, 1, 0, 0],
            [0, 0, -1/3, 1, 0, 1/3],
            [1/2, 1/3, 0, 1, 0, -1/3],
            [-1, -1, -1, 0, 0, 1/2],
            [0, 0, 0, 0, 0, 0],
            [0, -1/3, 1/3, -1/2, 0, 0]
        ]
        matching.calc()
        assert_allclose(matching.matrix, sample_relations, rtol=1e-2, atol=1e-2)
    def test_reduce(self):
        pool = Pool("sample.csv")
        matching = Matching(pool)
        matching.calc()
        matching.reduce()
        sample_relations = [
            [ 0, -1/3, 1, 0, 1/3],
            [ 1/3, 0, 1, 0, -1/3],
            [ -1, -1, 0, 0, 1/2],
            [0, 0, 0, 0, 0],
            [-1/3, 1/3, -1/2, 0, 0]
        ]
        assert_allclose(matching.reduced_matrix, sample_relations, rtol=1e-2, atol=1e-2)
        self.assertEqual(matching.dominance, [[1,0]])
        self.assertEqual(matching.dominated, [0])
    def test_save(self):
        pool = Pool("sample.csv")
        matching = Matching(pool)
        matching.calc()
        matching.save()
        matching.reduce()
        matching.save()
if __name__ == "__main__":
    unittest.main()


