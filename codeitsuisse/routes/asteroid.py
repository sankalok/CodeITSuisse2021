import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/asteroid', methods=['POST'])
def evaluateAsteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []

    for t in data['test_cases']:
        r = {}
        r['input'] = t
        uniqueS = ""
        for ch in r['input']:
            if(len(uniqueS) == 0):
                uniqueS += ch
            else:
                if uniqueS[len(uniqueS) - 1] != ch:
                    uniqueS += ch
        if(uniqueS == uniqueS[::-1]):
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
            for i in range(mid - 2, mid + 3):
                if(t[i-1] == t[i+1]):
                    r['origin'] = i
        result.append(r)

    result = json.dumps(result)
    logging.info("My result :{}".format(result))
    return result
