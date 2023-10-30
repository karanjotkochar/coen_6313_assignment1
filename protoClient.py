import batch_pb2, requests

batchRequest = batch_pb2.Request()

rfwId = input('Please Enter Request For Workload (RFW) ID: ')
benchmarkType = input('Please enter Benchmark Type from the following:\n1) DVD\n2) NDBench\n')
batchType= input('Please enter data type from the following:\n1) testing\n2) training\n')
workloadMetric = input('Please enter Workload Metric from the following:\n'
               '1) CPUUtilization_Average\n2) NetworkIn_Average\n3) NetworkOut_Average\n4) MemoryUtilization_Average\n')
batchId = int(input('Please enter the Batch Id (in integer): '))
batchUnit = int(input('Please enter the Batch Unit (in integer): '))
batchSize = int(input('Please enter the Batch Size (in integer): '))

batchRequest.rfwId = rfwId
batchRequest.benchmarkType = benchmarkType
batchRequest.batchType = batchType
batchRequest.workloadMetric = workloadMetric
batchRequest.batchId = batchId
batchRequest.batchUnit = batchUnit
batchRequest.batchSize = batchSize


res = requests.get("http://127.0.0.1:5000/getBatches?", headers={'Content-Type': 'application/protobuf'},
                                data=batchRequest.SerializeToString())

batchResponse = batch_pb2.Response.FromString(res.content)
print(batchResponse)
