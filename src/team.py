# このファイルでは構築に関する処理を記述

# プールを入力として受け取った上でそのプールで存在しうる全ての構築を出力
# ノード二つのインデックスの組を構築(Team)として保持
# インデックスじゃ出力する時にわからないのでインデックス→構築名をpandasのDataFrameで保持
import pandas as pd
import numpy as np

class TeamBuilder:
    def __init__(self, pool):
        self.pool = pool
        self.teams = pd.DataFrame(columns=["name", "node_index1", "node_index2"])

    def make_team(self):
        for i in range(len(self.pool.nodes)):
            for j in range(i+1, len(self.pool.nodes)):
                df = pd.DataFrame({"name": [self.pool.nodes[i]+self.pool.nodes[j]], "node_index1": [i], "node_index2": [j]})
                self.teams = pd.concat([self.teams, df], ignore_index=True)

    # 二つの構築に対して利得行列を返す
    def get_matrix(self,team1: list[int], team2: list[int]):

        matrix = np.zeros((len(team1), len(team2)))
        for i in range(len(team1)):
            for j in range(len(team2)):
                matrix[i][j] = self.pool.matrix[team1[i]][team2[j]]
        return matrix

if __name__ == "__main__":
    from pool import Pool
    team_builder = TeamBuilder(Pool("input/sample.csv"))
    team_builder.make_team()
    print(team_builder.teams["name"].tolist())


