import logging
import json
import sys

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def minCost(cost, m, n, x2, y2):
 
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(y2+1)] for x in range(x2+1)]
 
    tc[0][0] = cost[0][0]
 
    # Initialize first column of total cost(tc) array
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
 
    # Initialize first row of tc array
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
 
    # Construct rest of the tc array
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
 
    return tc[m][n]

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
        
        M = [[-1 for i in range(0, y2+1)] for j in range(0, x2+1)]
        rlM = [[-1 for i in range(0, y2+1)] for j in range(0, x2+1)]
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
        minC = minCost(grid, x2, y2, x2, y2)
        r["minimumCost"] = minC
        result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)



