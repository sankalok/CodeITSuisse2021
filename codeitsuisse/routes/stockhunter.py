import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = []
    r = dict()
    x1 = data["entryPoint"]["first"]
    y1 = data["entryPoint"]["second"]
    x2 = data["targetPoint"]["first"]
    y2 = data["targetPoint"]["second"]
    gD = data["gridDepth"]
    gK = data["gridKey"]
    hS = data["horizontalStepper"]
    vS = data["verticalStepper"]

    M = [[-1 for i in range(x2+1)] for j in range(y2+1)]
    rlM = [[-1 for i in range(x2+1)] for j in range(y2+1)]
    for i in range(0, x2+1):
        for j in range(0, y2+1):
            if((i == 0 and j == 0) or (i == x2 and y == y2)):
                riskIndex = 0
                riskLevel = ((riskIndex + gD) % gK)
                rlM[i][j] = riskLevel
                riskLevel %= 3
                if(riskLevel == 0):
                    M[i][j] = 'L'
                elif(riskLevel == 1):
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'H'
                continue
            elif(i != 0 and j == 0):
                riskIndex = i * hS
                riskLevel = ((riskIndex + gD) % gK)
                rlM[i][j] = riskLevel
                riskLevel %= 3
                if(riskLevel == 0):
                    M[i][j] = 'L'
                elif(riskLevel == 1):
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'H'
                continue
            elif(i == 0 and j != 0):
                riskIndex = j * vS
                riskLevel = ((riskIndex + gD) % gK)
                rlM[i][j] = riskLevel
                riskLevel %= 3
                if(riskLevel == 0):
                    M[i][j] = 'L'
                elif(riskLevel == 1):
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'H'
                continue
            else:
                riskIndex = rlM[i-1][j] * rLm[i][j-1]
                riskLevel = ((riskIndex + gD) % gK)
                rlM[i][j] = riskLevel
                riskLevel %= 3
                if(riskLevel == 0):
                    M[i][j] = 'L'
                elif(riskLevel == 1):
                    M[i][j] = 'M'
                else:
                    M[i][j] = 'H'
                continue
    r["gridMap"] = M
    r["minimumCost"] = 0
    result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
