import logging
import json

import random
from flask import request, jsonify
from itertool import permutations
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = dict()
    values = data['possible_values']
    slots = data['num_slots']
    count = 0
    for p in permutations(values, slots):
        result['answer'] = list(p)
        break
    @result['answer'] = sample
    #result['answer'] = ['f', 'j', 'e', 't', 'h']

    logging.info("My result :{}".format(result))
    return json.dumps(result)

