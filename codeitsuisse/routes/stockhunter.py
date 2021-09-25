import logging
import json
import sys

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def findMinCost(cost):
 
    # `M × N` matrix
    (M, N) = (len(cost), len(cost[0]))
 
    # `T[i][j]` maintains the minimum cost to reach cell (i, j) from cell (0, 0)
    T = [[0 for x in range(N)] for y in range(M)]
 
    # fill the matrix in a bottom-up manner
    for i in range(M):
        for j in range(N):
            T[i][j] = cost[i][j]
 
            # fill the first row (there is only one way to reach any cell in the
            # first row from its adjacent left cell)
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]
 
            # fill the first column (there is only one way to reach any cell in
            # the first column from its adjacent top cell)
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]
 
            # fill the rest with the matrix (there are two ways to reach any
            # cell in the rest of the matrix, from its adjacent
            # left cell or adjacent top cell)
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])
 
    # last cell of `T[][]` stores the minimum cost to reach destination cell
    # (M-1, N-1) from source cell (0, 0)
    return T[M - 1][N - 1]

@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    dataList = request.get_json()
    logging.info("data sent for evaluation {}".format(dataList))
    result = []
    for data in dataList:
        r = dict()
        x1 = data["entryPoint"]["first"]
        y1 = data["entryPoint"]["second"]
        x2 = data["targetPoint"]["first"]
        y2 = data["targetPoint"]["second"]
        gD = data["gridDepth"]
        gK = data["gridKey"]
        hS = data["horizontalStepper"]
        vS = data["verticalStepper"]
        
        M = []
        rlM = []
        grid = [[-1 for i in range(0, y2+1)] for j in range(0, x2+1)]

        for i in range(0, y2+1):
            riskIndex = i * vS
            riskLevel = ((riskIndex + gD) % gK)
            rlM[i][0] = riskLevel
            riskLevel %= 3
            if(riskLevel == 0):
                M[i][0] = "L"
                grid[i][0] = 3
            elif(riskLevel == 1):
                M[i][0] = "M"
                grid[i][0] = 2
            else:
                M[i][0] = "S"
                grid[i][0] = 1
        
        for i in range(1, x2+1):
            riskIndex = i * hS
            riskLevel = ((riskIndex + gD) % gK)
            rlM[0][i] = riskLevel
            riskLevel %= 3
            if(riskLevel == 0):
                M[0][i] = "L"
                grid[0][i] = 3
            elif(riskLevel == 1):
                M[0][i] = "M"
                grid[0][i] = 2
            else:
                M[0][i] = "S"
                grid[0][i] = 1

        for i in range(1, y2+1):
            for j in range(1, x2+1):
                riskIndex = rlM[i-1][j] * rlM[i][j-1]
                riskLevel = ((riskIndex + gD) % gK)
                rlM[i][j] = riskLevel
                riskLevel %= 3
                if(riskLevel == 0):
                    M[i][j] = "L"
                    grid[i][j] = 3
                elif(riskLevel == 1):
                    M[i][j] = "M"
                    grid[i][j] = 2
                else:
                    M[i][j] = "S"
                    grid[i][j] = 1

        r["gridMap"] = M
        minC = findMinCost(grid)
        r["minimumCost"] = minC
        result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)



