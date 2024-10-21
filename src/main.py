# このファイルではメインの処理を行う
from matching import Matching
from diagram import draw_diagram
from pool import Pool

pool = Pool("sample.csv")
pool.make_graph()
matching = Matching(pool)
matching.calc()
matching.reduce()
draw_diagram(matching.teams, matching.reduced_matrix, matching.dominated)
