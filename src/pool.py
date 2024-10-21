# このファイルではプールに関するクラスを定義する
import pandas as pd
import graphviz
from pathlib import Path

class Pool:
    def __init__(self, path: str):
        self.path = Path("input") / path
        self.read_csv()
        self.make_output_dir(path.split(".")[0])

    def read_csv(self):
        df = pd.read_csv(self.path)
        df.columns = ["source", "target"]
        self.nodes = list(set(df["source"]).union(set(df["target"])))
        self.nodes.sort()
        self.edges = df

    def make_graph(self):
        comment = "使用可能ポケモンのプール"
        dot = graphviz.Digraph(format="svg", comment=comment)
        for node in self.nodes:
            dot.node(node)
        for _, row in self.edges.iterrows():
            dot.edge(row["source"], row["target"])
        dot.render(str(self.output_path/"pool"), view=True)

    def make_matrix(self):
        self.matrix = [[0]*len(self.nodes) for _ in range(len(self.nodes))]
        for _, row in self.edges.iterrows():
            self.matrix[self.nodes.index(row["source"])][self.nodes.index(row["target"])] = 1
            self.matrix[self.nodes.index(row["target"])][self.nodes.index(row["source"])] = -1

    def make_output_dir(self, path):
        output_path = Path("output") / path
        if not output_path.exists():
            output_path.mkdir()
        self.output_path = output_path
