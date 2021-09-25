import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateRace():
    data = request.get_data()
    dataArr = data.split(',')
    return dataArr