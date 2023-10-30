from flask import Flask, request
from reponse import AllResponse
import batch_pb2

app = Flask(__name__)

@app.route('/getBatches', methods=['GET'])
def getBatches():
    batchRequest = batch_pb2.Request.FromString(request.data)
    batchResponse = batch_pb2.Response()
    batchObject = AllResponse(batchRequest.rfwId, batchRequest.benchmarkType, batchRequest.batchType, 
                        batchRequest.workloadMetric, batchRequest.batchId, batchRequest.batchUnit, batchRequest.batchSize)
    result = batchObject.binaryResult()
    batchResponse.rfwId = result['rfwId']
    batchResponse.lastBatchId = result['lastBatchId']
    batches = result['batches']
    
    
    for batch in batches:
        protoBatch = batch_pb2.Batch()
        samplesArr = []
        
        for i in range(0, len(batch)):
            samplesArr.append(batch[list(batch.keys())[0]])
        
        protoBatch.samples[:] = samplesArr
        batchResponse.batches.append(protoBatch)

    batchResponse.maximum = result['maximum']
    batchResponse.minimum = result['minimum']
    batchResponse.average = result['average']
    batchResponse.stDeviation = result['stDeviation']
    batchResponse.tenP = result['firstP']
    batchResponse.fiftyP = result['secondP']
    batchResponse.ninetyFiveP = result['thirdP']
    batchResponse.ninetyNineP = result['fourthP']

    print(batchResponse)

    if batchResponse is not None and batchResponse.lastBatchId is not None:
        serializedResult = batchResponse.SerializeToString()
        return serializedResult


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)