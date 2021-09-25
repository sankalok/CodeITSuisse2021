import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []

    for t in data['test_cases']:
        r = {}
        r['input'] = t
        counter = {}
        for ch in t:
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1
        score = 0
        for key in counter.keys():
            if(counter[key] <= 6):
                score += counter[key]
            elif(counter[key] > 6 and counter[key] < 10):
                score += counter[key] * 1.5
            elif(counter[key] >= 10):
                score += counter[key] * 2
        r['score'] = int(score)
        mid = len(t) // 2
        for i in range(mid - 1, mid + 2):
        if(t[i-1] == t[i+1]):
            r['origin'] = i
        result.append(r)

    result = json.dumps(result)
    logging.info("My result :{}".format(result))
    return result
