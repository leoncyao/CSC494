
import numpy as np

# n = 2 # size of base set
n = 5
m = 3 # number of sets


A = np.array([[1, 0, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]])
# A = np.random.randint(0,2,(m, n))
# A = np.ones((1, n))

m = A.shape[0]

x = np.zeros(n)

print(A)
print(A.sum(axis=0))
# d is degree of system
d = max(A.sum(axis=0))
print(d)

def isDangerous(S, nV_t, d):
    # S is a 1 x n row representing a set
    # V_t are the current NON fixed variables
    # d is the degree of the system
    return S[nV_t].sum() > d - 1

#!/usr/bin/env python3.7

import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
if __name__ == "__main__":


    try:

        # Create a new model
        model = gp.Model("beckFiala")
        model.params.NonConvex = 2
        # test = model.addVar(vtype=GRB.BINARY, name="x")
        # model.addConstr(test - 1, "test")        


        # represents delta_x
        variables = []
        for i in range(n):
            variables.append(model.addVar(lb=-100, ub =100, vtype=GRB.CONTINUOUS, name="x"+str(i)))
        # variables[0].start = 1
        # variables[0].start = -1
        # for i in range(n):
            # model.addConstr(variables[i] <= -0.00001, "+C" + str(i))        
            # model.addConstr(variables[i] >= -1, "-C" + str(i))        

        


        # print("check")

        for i in range(m):
            print(i)
            if isDangerous(A[i , :], np.argwhere(abs(x) < 1),d):
                print(A[i, :], " is dangerous")
                nonfixed =  [variables[j] for j in range(n) if abs(x[j]) < 1 and A[i, j] == 1]
                print(len(nonfixed))
                model.addConstr(quicksum(nonfixed) == 0, "D" + str(i))        
                # model.addConstr(quicksum(nonfixed) <= 0.001, "+D" + str(i))        
                # model.addConstr(quicksum(nonfixed) >= -0.001, "-D" + str(i))        


        # Set objective
        model.setObjective(quicksum([v * v for v in variables]), GRB.MAXIMIZE)

        # m.setParam("SolFiles", "test");

        # Optimize model
        model.optimize()

        model.write("file.lp")
        model.write("out.sol")


        soln = np.array([v.x for v in model.getVars()])
        print(soln)

        soln = soln / np.amax(np.abs(soln))

        print(soln)

        x += soln 
        # for v in model.getVars():
        #     print('%s %g' % (v.varName, v.x))

        # print('Obj: %g' % model.objVal)

    except gp.GurobiError as e:
        print('Error code ' + str(e.errno) + ': ' + str(e))

    except AttributeError:
        print('Encountered an attribute error')












