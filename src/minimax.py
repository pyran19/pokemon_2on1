import pulp
import numpy as np

def minimax(A,alive=[]):
    n,m=A.shape
    lp = pulp.LpProblem(sense=pulp.LpMaximize)
    v = pulp.LpVariable("v") 
    x = [ pulp.LpVariable("x_"+str(i)) for i in range(m) ]
    for i in range(m):
        lp += v <= pulp.lpDot(A[:,i], x)
    for i in range(m):
        lp += x[i] >= 0 if i not in alive else x[i] >= 1e-4
        lp += x[i] <= 1
    lp += pulp.lpSum(x) == 1
    lp += v
    lp.solve(pulp.PULP_CBC_CMD(msg=False))
    x = np.array([ x[i].value() for i in range(m) ])

    return x,v.value()