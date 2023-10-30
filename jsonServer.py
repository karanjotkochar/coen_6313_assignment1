from flask import Flask, request, json
from reponse import AllResponse
import json

app = Flask(__name__)


@app.route('/getBatches', methods=['GET'])
def getBatches():
    rfwId = request.json['rfwId']
    benchmarkType = request.json['benchmarkType']
    batchType = request.json['batchType']
    workloadMetric = request.json['workloadMetric']
    batchId = request.json['batchId']
    batchUnit = request.json['batchUnit']
    batchSize = request.json['batchSize']

    batchObject = AllResponse(rfwId, benchmarkType, batchType, workloadMetric, batchId, batchUnit, batchSize)
    result = batchObject.sendJsonResults()
    
# Serializing json and writing json file
    if result is not None:
        # jsonOutput = json.dumps(result)
        # with open( "datafile.json" , "w" ) as output:
        #     output.write(jsonOutput)
        # return jsonOutput
        return json.dumps(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
    