import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stig/perry', methods=['POST'])
def evaluateStig():
    dataList = request.get_json()
    logging.info("data sent for evaluation {}".format(dataList))
    
    result = []
    
    for data in dataList:
        r = {'p' : 1, 'q' : 50000000}
        for d in data:
            r['p'] = max(r['p'], d['from'])
            r['q'] = min(r['q'], d['to'])
        result.append(r)


    logging.info("My result :{}".format(result))
    return json.dumps(result)
