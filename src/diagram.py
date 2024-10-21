# このファイルでは計算結果の相性関係を図示する

import graphviz


def draw_diagram(teams,path,matrix,dominated=[]):
    teams = teams.drop(index=dominated)
    n = len(matrix)
    dot = graphviz.Digraph(format="svg")
    for i in range(n):
        dot.node(teams.iloc[i]["name"])
    for i in range(n):
        for j in range(i+1, n):
            if round(matrix[i,j], 2) > 0:
                dot.edge(teams.iloc[i]["name"], teams.iloc[j]["name"], label=str(round(matrix[i,j], 2)))
            elif round(matrix[i,j], 2) < 0:
                dot.edge(teams.iloc[j]["name"], teams.iloc[i]["name"], label=str(round(-matrix[i,j], 2)))
    dot.render(str(path/"diagram"), view=True)
