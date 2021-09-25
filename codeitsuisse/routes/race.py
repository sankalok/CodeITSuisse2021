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
    d = ",".join(arr)
    return str(d)