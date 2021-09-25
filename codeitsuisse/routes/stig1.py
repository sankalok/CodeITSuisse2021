import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stig/perry', methods=['POST'])
def evaluateStig1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    from = []
    to = []
    result = []
    for q in data['questions']:
        from.append(q['from'])
        to.append(q['to'])
    
    r = dict()
    r['p'] = max(from)
    r['q'] = min(to)
    result.append(r)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
