import requests
import json

rfwId = input('Please Enter Request For Workload (RFW) ID: ')
benchmarkType = input('Please enter Benchmark Type from the following:\n1) DVD\n2) NDBench\n')
batchType= input('Please enter data type from the following:\n1) testing\n2) training\n')
workloadMetric = input('Please enter Workload Metric from the following:\n'
               '1) CPUUtilization_Average\n2) NetworkIn_Average\n3) NetworkOut_Average\n4) MemoryUtilization_Average\n')
batchId = input('Please enter the Batch Id (in integer): ')
batchUnit = input('Please enter the Batch Unit (in integer): ')
batchSize = input('Please enter the Batch Size (in integer): ')

res = requests.get("http://127.0.0.1:5000/getBatches?",
                   json={"rfwId": rfwId,
                         "benchmarkType": benchmarkType,
                         "batchType":batchType,
                         "workloadMetric": workloadMetric,
                         "batchId": batchId,
                         "batchUnit": batchUnit,
                         "batchSize": batchSize}
                   )
if res.status_code == 200:
    print(" RFW ID: ", res.json()['rfwId'])
    print(" Last Batch ID: ", res.json()['lastBatchId'])
    print(" Data Samples Requested: ", res.json()['samples'])
    print(" Data Analytics - Maximum value: ", res.json()['maximum'])
    print(" Data Analytics - Minimum value: ", res.json()['minimum'])
    print(" Data Analytics - Average value: ", res.json()['average'])
    print(" Data Analytics - Standard Deviation: ", res.json()['stDeviation'])
    print(" Data Analytics - 10p: ", res.json()['firstP'])
    print(" Data Analytics - 50p: ", res.json()['secondP'])
    print(" Data Analytics - 95p: ", res.json()['thirdP'])
    print(" Data Analytics - 99p: ", res.json()['fourthP'])
   

