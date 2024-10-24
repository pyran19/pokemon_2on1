# このファイルでは構築作成のゲームについてナッシュ均衡を求める

from minimax import minimax


class NashTeamAnalyser:
    def __init__(self, A):
        self.A = A
    def calc(self,alive=[]):
        x,v =minimax(self.A,alive)
        if round(v,2) == 0:
            self.effective_team , self.ineffective_team = self.judgeEffective(x)
        else:
            raise ValueError("対称ゲームなので0になるはず")
    def get_effective_team(self):
        # 効率的なチームのindexを返す
        return self.effective_team
    def get_ineffective_team(self):
        # 非効率的なチームのindexを返す
        return self.ineffective_team
    def judgeEffective(self,teams):
        # チームが効率的かどうかを判定する
        effective_team = []
        ineffective_team = []
        for index,team in enumerate(teams):
            if team >= 1e-4:
                effective_team.append(index)
            else:
                ineffective_team.append(index)
        return effective_team , ineffective_team

