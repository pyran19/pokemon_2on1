# このファイルでは選出ゲームについて記述

import pulp
import numpy as np



#線形計画法
def selection(A):
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
    x = np.array([ x[i].value() for i in range(m) ])
    
    return v.value()


