import logging
import json

from flask import request, jsonify
import numpy
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateRace():
    data = request.get_data()
    arr = data.split(',')
    numpy.random.permutation(arr)
    d = str(arr[0]) + ',' + str(arr[1]) + ',' +str(arr[2]) + ',' +str(arr[3]) + ',' +str(arr[4]) + ',' +str(arr[5]) + ',' +str(arr[6]) + ',' +str(arr[7]) + ',' +str(arr[8]) + ',' +str(arr[9])
    return d