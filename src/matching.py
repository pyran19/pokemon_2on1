# このファイルでは他のモジュールを結合させてチーム間の相性関係を計算する
from pool import Pool
from team import TeamBuilder
from selection import selection
import numpy as np


class Matching:
    def __init__(self, pool):
        self.pool = pool
        self.output_path = pool.output_path
        self.dominated = [] # 支配されるチームのindexを記録
        self.dominance = [] # [[i,j]]の形でiがjを支配する関係を記録
        self.reduced_matrix = None
    def calc(self):
        self.pool.make_matrix()
        self.team_builder = TeamBuilder(self.pool)
        self.team_builder.make_team()
        self.teams=self.team_builder.teams
        self.matrix = np.zeros((len(self.teams), len(self.teams)))
        for i, row in self.teams.iterrows():
            team1 = [row["node_index1"], row["node_index2"]]
            for j, row2 in self.teams.iloc[i+1:].iterrows():
                team2 = [row2["node_index1"], row2["node_index2"]]
                matrix = self.team_builder.get_matrix(team1, team2)
                v = selection(matrix)
                self.matrix[i,j] = v
                self.matrix[j,i] = -v
    def reduce(self, to_remove):
        keep = [i for i in range(len(self.matrix)) if i not in to_remove]
        self.reduced_matrix = self.matrix[np.ix_(keep, keep)]
    def reduce_dominated(self):
        n = len(self.matrix)
        to_remove = set(self.dominated)
        alive = [i for i in range(n) if i not in self.dominated]
        for i_alive, i in enumerate(alive):
            for j_alive, j in enumerate(alive[i_alive+1:]):
                if all(self.matrix[i, k] == self.matrix[j, k] for k in alive ):
                    self.dominance.append([i,j])
                    to_remove.add(j)
                elif all(self.matrix[i, k] <= self.matrix[j, k] for k in alive ):
                    self.dominance.append([j,i])
                    to_remove.add(i)
                elif all(self.matrix[i, k] >= self.matrix[j, k] for k in alive ):
                    self.dominance.append([i,j])
                    to_remove.add(j)
        self.reduce(to_remove)
        self.dominated = list(to_remove)
    def repreat_reduce_dominated(self):
        while True:
            n = len(self.dominated)
            self.reduce_dominated()
            if len(self.dominated) == n:
                break
    def save(self):
        self.teams.to_csv(self.output_path / "teams.csv", index=True)
        np.savetxt(self.output_path / "full_matrix.csv", self.matrix, delimiter=",")
        if self.reduced_matrix is not None:
            np.savetxt(self.output_path / "reduced_matrix.csv", self.reduced_matrix, delimiter=",")
            with open(self.output_path / "dominance.txt", "w") as f:
                for d in self.dominance:
                    f.write(f"{self.teams.iloc[d[0]]['name']} dominates {self.teams.iloc[d[1]]['name']}\n")








