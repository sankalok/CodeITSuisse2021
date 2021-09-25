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
        r = dict()
        r['input'] = t
        uniqueS = []
        for ch in r['input']:
            if (len(uniqueS) == 0):
                uniqueS += [ch]
            else:
                if uniqueS[len(uniqueS) - 1] != ch:
                    uniqueS += [ch]
        indexes = [0] * len(uniqueS)
        i = 0
        ch = ''
        for j in range(0, len(r['input'])):
            if (j == 0):
                indexes[i] = j
            if (r['input'][j] != uniqueS[i]):
                indexes[i + 1] = j
                i += 1

        s = ''.join(uniqueS)  
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C, R = i, i + P[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        start = (centerIndex  - maxLen)//2
        end = (centerIndex  + maxLen)//2
        uniqueS = []
        s = s[start:end]
        for i in s:
            uniqueS += [i]
        score = 0
        j = end
        indexes += [len(r['input'])]
        for i in range(start, (end + start) // 2):
            rng = indexes[i + 1] - indexes[i] + indexes[j] - indexes[j - 1]
            if (rng <= 6):
                score += rng
            elif (rng >= 7 and rng <= 9):
                score += (1.5 * rng)
            elif (rng >= 10):
                score += (2 * rng)
            j -= 1
        rng = (indexes[(start + end - 1) // 2 + 1] - indexes[(start + end - 1) // 2])
        if (rng <= 6):
            score += rng
        elif (rng >= 7 and rng <= 9):
            score += (1.5 * rng)
        elif (rng >= 10):
            score += (2 * rng)
        mid = (indexes[(start + end - 1) // 2] + indexes[(start + end - 1) // 2 + 1]) // 2
        r['score'] = int(score)
        r['origin'] = mid
        result.append(r)


    logging.info("My result :{}".format(result))
    return json.dumps(result)
