# このファイルではメインの処理を行う
from matching import Matching
from diagram import draw_diagram
from pool import Pool

pool = Pool("7pokemon1.csv")
pool.make_graph()
matching = Matching(pool)
matching.calc()
matching.reduce()
matching.save()
draw_diagram(matching.teams, pool.output_path, matching.reduced_matrix, matching.dominated)
