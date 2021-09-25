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
        
        for q in data['questions']:
            fr.append(q['from'])
            t.append(q['to'])
    
        r = dict()
        r['p'] = max(fr)
        r['q'] = min(t)
        result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
