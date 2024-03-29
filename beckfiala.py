
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
def get_A(m,n):
    A = np.around(np.random.rand(m, n), decimals=1)
    w = 0.5
    # m = A.shape[0]
    x = np.zeros(n)
    d = max(A.sum(axis=0))

    return x,d, A, m, n
# n = 2 # size of base set
# n = 23
# m = 5 # number of sets

# np.random.permutation()
# A = np.array([[1, 0, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]])
# A = np.random.randint(0,2,(m, n))
# A = np.random.rand(0,2,(m, n))
# A = np.around(np.random.rand(m, n), decimals=1)

# B = "1 1 1 0 0 1 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 1][1 0 0 0 1 1 0 1 1 0 0 1 1 0 1 0 0 0 1 0 0 0 1][1 0 0 0 1 1 0 0 0 0 0 0 1 0 1 1 0 1 1 1 1 1 0][1 1 1 0 1 1 1 0 0 1 0 0 0 1 0 1 1 1 1 0 0 1 1][1 0 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 1 0 1 0 0 0".split("][")
# C = []
# print(B)
# for row in B:
    # print(row)
    # C.append(list(map(int, row.split(" "))))
# print(C)

# w = 0.5
# A = np.random.choice(2, (m, n), p=[w, 1 - w])
# A = np.array(C) 
# m = A.shape[0]

# x = np.zeros(n)

# print(A)
# print(A.sum(axis=0))
# d is degree of system
# d = max(A.sum(axis=0))

def isDangerous(S, nV_t, d):
    # S is a 1 x n row representing a set
    # V_t are the current NON fixed variables
    # d is the degree of the system
    print("plz don't be a decimal: ", S[nV_t].sum())
    return S[nV_t].sum() > d

def get_variables(max_iters, t):
    x = get_A(5, 23)[0] 
    d = get_A(5, 23)[1]
    A = get_A(5, 23)[2]
    m = get_A(5, 23)[3]
    n = get_A(5, 23)[4]
    while np.sum(np.abs(x)) < n and t < max_iters:
        # Create a new model
        model = gp.Model("beckFiala")
        print("current colouring: \n", x)
        # print("current colouring: ", list(map(int, x)))
        model.params.LogToConsole = 0
        model.params.NonConvex = 2

        # represents delta_x
        variables = []
        for i in range(n):
            # if (abs(x[i]) < 1):
            if (abs(abs(x[i]) - 1) > 0.00001):
                # print("adding variable x" + str(i))
                # print("x{}: ".format(i), abs(x[i]))
                variables.append(model.addVar(lb=-100, ub =100, vtype=GRB.CONTINUOUS, name="x"+str(i)))
            else:
                variables.append(x[i])
        
        for i in range(m):
            # if isDangerous(A[i , :], np.argwhere(abs(x) < 1),d):
            if isDangerous(A[i , :], np.argwhere(abs(abs(x) - 1) > 0.00001),d):
                # print(A[i, :], " is dangerous")
                nonfixed =  [variables[j] for j in range(n) if abs(x[j]) < 1 and A[i, j] == 1]
                model.addConstr(quicksum(nonfixed) == 0, "D" + str(i))
    return variables
#!/usr/bin/env python3.7

import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
if __name__ == "__main__":
    results = []
    for i in range (100):
        x = get_A(5, 23)[0] 
        d = get_A(5, 23)[1]
        A = get_A(5, 23)[2]
        m = get_A(5, 23)[3]
        n = get_A(5, 23)[4]
        max_iters = 100
        t = 0
        while np.sum(np.abs(x)) < n and t < max_iters:
            # Create a new model
            model = gp.Model("beckFiala")
            # print("current colouring: \n", x)
            # print("current colouring: ", list(map(int, x)))
            model.params.LogToConsole = 0
            model.params.NonConvex = 2

            # represents delta_x
            variables = []
            for i in range(n):
                # if (abs(x[i]) < 1):
                if (abs(abs(x[i]) - 1) > 0.00001):
                    # print("adding variable x" + str(i))
                    # print("x{}: ".format(i), abs(x[i]))
                    variables.append(model.addVar(lb=-100, ub =100, vtype=GRB.CONTINUOUS, name="x"+str(i)))
                else:
                    variables.append(x[i])
        
            for i in range(m):
                # if isDangerous(A[i , :], np.argwhere(abs(x) < 1),d):
                if isDangerous(A[i , :], np.argwhere(abs(abs(x) - 1) > 0.00001),d):
                    # print(A[i, :], " is dangerous")
                    nonfixed =  [variables[j] for j in range(n) if abs(x[j]) < 1 and A[i, j] == 1]
                    model.addConstr(quicksum(nonfixed) == 0, "D" + str(i))        
        
            # variables = get_variables(100, 0)
            model.setObjective(quicksum([v * v for v in variables]), GRB.MAXIMIZE)

            # Optimize model
            model.optimize()

            # print(model.)
            print("test: ", GRB.OPTIMAL)

            model.write("file.lp")
            print("status:", model.status)

            if not model.status == GRB.OPTIMAL:
                print("no solution")
                break
                model.write("out.sol")


            soln = np.zeros(n); # soln repsents deltax
                            # soln[x] = 0 if x[i] is already fixed (x[i] = 1 or -1)
            for v in model.getVars():
                index = int(v.varName[1:])
                soln[index] = v.x
                # print(index)
        
            # print(soln)
            soln = soln / np.amax(np.abs(soln))

            # print("dx: ", list(map(round, soln)))
            # print("dx: ", soln)

            nonfixedindices = np.argwhere(abs(x) < 1)
            nonfixedindices = np.reshape(nonfixedindices, nonfixedindices.shape[0])

            limit = np.zeros((n, 1))

            for k in nonfixedindices:
                limit[k] = abs(x[k] + soln[k])

            # soln is delta_x, to figure 

            q = np.argmax(limit)
            # print("q1: ", q)
            # Lambda = abs(((1 - x[q]) / soln[q]))
            Lambda1 = min(abs(((1 - x[q]) / soln[q])), abs(((x[q] + 1) / soln[q])))

            randomized = sys.argv[1] == "random"
            if randomized:
                nonfixedindices = np.argwhere(abs(x) < 1)
                nonfixedindices = np.reshape(nonfixedindices, nonfixedindices.shape[0])

                limit = np.zeros((n, 1))

                # goes the other way
                for k in nonfixedindices:
                    limit[k] = abs(x[k] - soln[k])

                # soln is delta_x, to figure 

                q = np.argmax(limit)

                print("q2: ",q )
                # Lambda = abs(((1 - x[q]) / soln[q]))
                Lambda2 = -min(abs(((1 - x[q]) / soln[q])), abs(((x[q] + 1) / soln[q])))

                # should pick lambda with probability p = -lambda2 / (lambda1 - lambda2) to keep
                # expection of x(t+1) the same
                print("q: {}, x[{}]: {}, soln[{}] {}".format(q, q, x[q], q, soln[q]))
                prob = -Lambda2 / (Lambda1 - Lambda2)
                print(prob)
                Lambda = np.random.choice([Lambda1, Lambda2], 1, p=[-Lambda2 / (Lambda1 - Lambda2), 1 - (-Lambda2 / (Lambda1 - Lambda2))])
            else:
                Lambda = Lambda1

            # print("lambda: ", Lambda)
            # x += abs(((1 - x[q]) / soln[q])) * soln
            x += Lambda * soln
            t += 1

        # print("final colouring: ", list(map(round, x)))
        # print("final colouring: ", x)

        disc = 0
        for i in range(m):
            temp_disc = 0
            for j in range(n):
                if A[i, j] == 1:
                    temp_disc += x[j]
            if abs(temp_disc) > disc:
                disc = abs(temp_disc)

    # print("final discrepancy is: " , disc)
    # print("2*degree - 1: ", 2*d - 1)
    # print(disc <= 2*d - 1)
        results.append(disc <= 2*d - 1)
    for i in range(len(results)):
        if not results[i]:
            print("The {}th is not correct".format(i))
            break
    print("All correct")








