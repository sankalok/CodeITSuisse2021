import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    dataList = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    for data in dataList:
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
        
        M = [[-1 for j in range(0, y2+1)] for i in range(0, x2+1)]
        rlM = [[-1 for j in range(0, y2+1)] for i in range(0, x2+1)]
        for i in range(0, y2+1):
            for j in range(0, x2+1):
                if((i == 0 and j == 0) or (i == x2 and j == y2)):
                    riskIndex = 0
                    riskLevel = ((riskIndex + gD) % gK)
                    rlM[j][i] = riskLevel
                    riskLevel %= 3
                    print(riskLevel)
                    if(riskLevel == 0):
                        M[j][i] = 'L'
                    elif(riskLevel == 1):
                        M[j][i] = 'M'
                    else:
                        M[j][i] = 'S'
                    continue
                elif(i != 0 and j == 0):
                    riskIndex = i * hS
                    riskLevel = ((riskIndex + gD) % gK)
                    rlM[j][i] = riskLevel
                    riskLevel %= 3
                    if(riskLevel == 0):
                        M[j][i] = 'L'
                    elif(riskLevel == 1):
                        M[j][i] = 'M'
                    else:
                        M[j][i] = 'S'
                    continue
                elif(i == 0 and j != 0):
                    riskIndex = j * vS
                    riskLevel = ((riskIndex + gD) % gK)
                    rlM[j][i] = riskLevel
                    riskLevel %= 3
                    if(riskLevel == 0):
                        M[j][i] = 'L'
                    elif(riskLevel == 1):
                        M[j][i] = 'M'
                    else:
                        M[j][i] = 'S'
                    continue
                else:
                    riskIndex = rlM[j-1][i] * rlM[j][i-1]
                    riskLevel = ((riskIndex + gD) % gK)
                    rlM[i][j] = riskLevel
                    riskLevel %= 3
                    if(riskLevel == 0):
                        M[j][i] = 'L'
                    elif(riskLevel == 1):
                        M[j][i] = 'M'
                    else:
                        M[j][i] = 'S'
                    continue
        r["gridMap"] = M
        r["minimumCost"] = 0
        result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)