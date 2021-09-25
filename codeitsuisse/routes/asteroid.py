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
    '''
    for t in data['test_cases']:
        r = dict()
        r['input'] = t
        uniqueS = []
        for ch in r['input']:
            if(len(uniqueS) == 0):
                uniqueS += [ch]
            else:
                if uniqueS[len(uniqueS) - 1] != ch:
                    uniqueS += [ch]
        indexes = [0]*len(uniqueS)
        i = 0
        ch = ''
        for j in range(0, len(r['input'])):
            if(j == 0):
                indexes[i] = j
            if(r['input'][j] != uniqueS[i]):
                indexes[i+1] = j
            i += 1
        s = 0
        l = 1
        for i in range(0, len(uniqueS)):
            for j in range(i, len(uniqueS)):
                check = 1
                for k in range(0, (i-j)//2 + 1):
                    if(uniqueS[i+k] != uniqueS[j-k]):
                        check = 0
                if(check != 0 and (j-i+1) > l):
                    s = i
                    l = j-i+1
        start = s
        end = s+l
        score = 0
        j = end
        indexes += [len(r['input'])]
        for i in range(start, (end+start)//2):
            rng = indexes[i+1] - indexes[i] + indexes[j] - indexes[j-1]
            if(rng <= 6):
                score += rng
            elif(rng >= 7 and rng <= 9):
                score += (1.5 * rng)
            elif(rng >= 10):
                score += (2 * rng)
            j -= 1
        rng = (indexes[(start+end-1)//2 + 1] - indexes[(start+end-1)//2])
        if(rng <= 6):
            score += rng
        elif(rng >= 7 and rng <= 9):
            score += (1.5 * rng)
        elif(rng >= 10):
            score += (2 * rng)
        mid = (indexes[(start+end-1)//2] + indexes[(start+end-1)//2 + 1]) // 2
        r['score'] = int(score)
        r['mid'] = mid
        result.append(r)
    '''
    logging.info("My result :{}".format(result))
    return json.dumps(data)
