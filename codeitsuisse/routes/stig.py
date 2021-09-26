import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stig/perry', methods=['POST'])
def evaluateStig():
    dataList = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    
    result = []
    for data in dataList:
        fr = []
        t = []
        r = {'p': 1, 'q': 500000000}
        count = 1
        for q in data['questions']:
            if(count % 2 == 1):
                r['p'] = min(r['p'], q['from'])
                r['q'] = max(r['q'], q['to'])
        result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
