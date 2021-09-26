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
        r['p'] = max(r['p'], data[0]['from'])
        r['q'] = min(r['q'], data[0]['to'])
        result.append(r)


    logging.info("My result :{}".format(result))
    return json.dumps(result)
