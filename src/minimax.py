import pulp
import numpy as np

def minimax(A):
    n,m=A.shape
    lp = pulp.LpProblem(sense=pulp.LpMaximize)
    v = pulp.LpVariable("v") 
    x = [ pulp.LpVariable("x_"+str(i)) for i in range(m) ]
    for i in range(m):
        lp += v <= pulp.lpDot(A[:,i], x)
    for i in range(m):
        lp += x[i] >= 0
        lp += x[i] <= 1
    lp += pulp.lpSum(x) == 1
    lp += v
    lp.solve(pulp.PULP_CBC_CMD(msg=False))
    x = np.array([x[i].value() for i in range(m)])
    return x,v.value()
    
def minimax_zero(A,optimal_v):
    n,m=A.shape
    # 各xiの最大値を求める
    zero_in_all_equilibria = []
    for j in range(m):
        lp_max_x = pulp.LpProblem(sense=pulp.LpMaximize)
        x_max = [ pulp.LpVariable("x_"+str(i)) for i in range(m) ]
        for i in range(m):
            lp_max_x +=  pulp.lpDot(A[:,i], x_max) >= optimal_v
        for i in range(m):
            lp_max_x += x_max[i] >= 0
            lp_max_x += x_max[i] <= 1
        lp_max_x += pulp.lpSum(x_max) == 1
        lp_max_x += x_max[j]  # j番目の変数を最大化
        lp_max_x.solve(pulp.PULP_CBC_CMD(msg=False))
        
        if x_max[j].value() < 1e-10:  # 数値誤差を考慮
            zero_in_all_equilibria.append(j)
    
    return zero_in_all_equilibria

