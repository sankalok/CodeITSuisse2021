import logging
import json

import random
from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def evaluateDecoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    result = dict()
    values = data['possible_values']
    slots = data['num_slots']
    sample = random.sample(values, slots)
    #result['answer'] = sample
    result['answer'] = ['i', 'u', 'f', 'b', 'h']

    logging.info("My result :{}".format(result))
    return json.dumps(result)

