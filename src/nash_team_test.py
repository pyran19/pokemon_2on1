import nash_team
import unittest
import numpy as np

class TestNashTeam(unittest.TestCase):
    def test_single_nash(self):
        # 単一のナッシュ均衡が存在する場合
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
    def test_multiple_nash(self):
        # 複数のナッシュ均衡が存在する場合
        A = np.array([[0., 0., -0.5, 1.,0., 0.],
        [0., 0., -0.33, 1.,0.,  0.33],
        [0.5, 0.33, 0., 1.,0.,  -0.33],
        [-1., -1., -1., 0.,0.,  0.5],
        [0.,0.,0.,0.,0.,0.],
        [0., -0.33, 0.33, -0.5,  0.,0.]])
        analyser = nash_team.NashTeamAnalyser(A)
        analyser.calc()
        ineffective_team = analyser.get_ineffective_team()
        self.assertEqual(ineffective_team, [0,3])
        effective_team = analyser.get_effective_team()
        self.assertEqual(effective_team, [1, 2, 4, 5])
    @unittest.skip("skip")
    def test_multiple_nash2(self):
        # 複数のナッシュ均衡が存在する場合
        A = np.array([
        [0., -0.33, 0., -0.5, 0.33, 1., 0., 0.33, 0., 0.],
        [0.33, 0., 0.5, 0., -0.33, 1., -0.33, 0., 0., 0.],
        [0., -0.5, 0., -0.33, 0., 1., 0.33, 0., 0., 0.33],
        [0.5, 0., 0.33, 0., 0., 1., 0., -0.33, 0., -0.33],
        [-0.33, 0.33, 0., 0., 0., 0., 0., 0., 0., 0.],
        [-1., -1., -1., -1., 0., 0., 0., 0., 0.5, 0.],
        [0., 0.33, -0.33, 0., 0., 0., 0., 0., 0., 0.],
        [-0.33, 0., 0., 0.33, 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., -0.5, 0., 0., 0., 0.],
        [0., 0., -0.33, 0.33, 0., 0., 0., 0., 0., 0.]
        ])
        analyser = nash_team.NashTeamAnalyser(A)
        analyser.calc()
        ineffective_team = analyser.get_ineffective_team()
        self.assertEqual(ineffective_team, [5,8])
        effective_team = analyser.get_effective_team()
        self.assertEqual(effective_team, [0,1,2,3,4,6,7])
if __name__ == '__main__':
    unittest.main()
