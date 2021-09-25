import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])
def evaluateRace():
    data = request.get_data()
    return "Simon Sprayberry,Lucy Lippold,Lamont Lasch,Damien Degraff,Boris Batts,Dominique Deshon,Annamarie Ahern,Jewel Jaegar,Lindsey Lamb,Judi Jacques"