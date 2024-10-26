# このファイルではメインの処理を行う
from matching import Matching
from diagram import draw_diagram
from pool import Pool
import nash_team

pool = Pool("sample.csv")
pool.make_graph()
matching = Matching(pool)
matching.calc()
analyser = nash_team.NashTeamAnalyser(matching.matrix)
analyser.calc()
reduced = analyser.get_ineffective_team()
matching.reduce(reduced)
matching.save()
draw_diagram(matching.teams, pool.output_path, matching.reduced_matrix, reduced)
#draw_diagram(matching.teams, pool.output_path, matching.matrix, [])
