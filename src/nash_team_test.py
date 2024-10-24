import nash_team
import unittest
import numpy as np

class TestNashTeam(unittest.TestCase):
    def test_judgeEffective(self):
        dummy_matrix = np.array([[0., 0.],
                                [0., 0.]])
        analyser = nash_team.NashTeamAnalyser(dummy_matrix)
        x=[0.4,0,0.3,0.2,0,0.1]
        effective_team , ineffective_team = analyser.judgeEffective(x)
        self.assertEqual(set(effective_team+ineffective_team), set(range(len(x))))
        self.assertEqual(effective_team, [0, 2, 3, 5])
        self.assertEqual(ineffective_team, [1,4])
    def test_nash_team(self):
        A = np.array([[0., 0., -0.5, 1., 0.],
        [0., 0., -0.33, 1.,  0.33],
        [0.5, 0.33, 0., 1.,  -0.33],
        [-1., -1., -1., 0.,  0.5],
        [0., -0.33, 0.33, -0.5,  0.]])
        analyser = nash_team.NashTeamAnalyser(A)
        analyser.calc()
        ineffective_team = analyser.get_ineffective_team()
        self.assertEqual(ineffective_team, [0,3])
        effective_team = analyser.get_effective_team()
        self.assertEqual(effective_team, [1, 2, 4])
    def test_specified_connected_team(self):
        A = np.array([[0., 0., -0.5, 1., 0.],
        [0., 0., -0.33, 1.,  0.33],
        [0.5, 0.33, 0., 1.,  -0.33],
        [-1., -1., -1., 0.,  0.5],
        [0., -0.33, 0.33, -0.5,  0.]])
        analyser = nash_team.NashTeamAnalyser(A)
        analyser.calc(alive=[1])
        ineffective_team = analyser.get_ineffective_team()
        self.assertEqual(ineffective_team, [0,3])
        effective_team = analyser.get_effective_team()
        self.assertEqual(effective_team, [1, 2, 4])

if __name__ == '__main__':
    unittest.main()
