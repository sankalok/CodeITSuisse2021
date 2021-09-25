import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])
def evaluateStockHunter():
    dataList = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    
    logging.info("My result :{}".format(result))
    return json.dumps(dataList)



