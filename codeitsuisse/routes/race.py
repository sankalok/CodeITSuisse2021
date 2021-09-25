import logging
import json

from flask import request, jsonify
import numpy
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateRace():
    data = request.get_json()
    d = data.split(",")
    d2 = random.sample(d, len(d))
    d3 = ",".join(d2)
    return d3