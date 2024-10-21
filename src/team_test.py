import unittest
from pool import Pool
from team import TeamBuilder
import numpy as np
from numpy.testing import assert_array_equal

class TestTeam(unittest.TestCase):
    def test_make_team(self):
        pool = Pool("input/sample.csv")
        team_builder = TeamBuilder(pool)
        team_builder.make_team()
        self.assertEqual(len(team_builder.teams), 6)
        sample_teams={"AB", "BC", "CD", "AD", "AC", "BD"}
        self.assertEqual(set(team_builder.teams["name"].tolist()), sample_teams)
    def test_get_matrix(self):
        pool = Pool("input/sample.csv")
        pool.make_matrix()
        team_builder = TeamBuilder(pool)
        team_builder.make_team()
        assert_array_equal(team_builder.get_matrix([0, 1], [1, 2]), np.array([[1, 1], [0, 1]]))
        assert_array_equal(team_builder.get_matrix([0, 1], [2, 3]), np.array([[1, -1], [1, 0]]))
        assert_array_equal(team_builder.get_matrix([0, 3], [2, 3]), np.array([[1, -1], [-1, 0]]))

if __name__ == "__main__":
    unittest.main()



