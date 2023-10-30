import pandas as pd
import statistics
import numpy as np
from statistics import mean
import json


class AllResponse:
# Constructor
    def __init__(self, rfwId, benchmarkType, batchType, workloadMetric, batchId, batchUnit, batchSize):
        self.rfwId = rfwId
        self.benchmarkType = benchmarkType
        self.batchType = batchType
        self.workloadMetric = workloadMetric
        self.batchId = int(batchId)
        self.batchUnit = int(batchUnit)
        self.batchSize = int(batchSize)
        self.csvData = pd.read_csv("./data/" + benchmarkType + "-" + batchType + ".csv")


# Response
    def sendJsonResults(self):
        samples = self.totalSamples()
        (batches, lastBatchId) = self.createBatches()
        batches = self.convertToDict(batches)
        maximum = self.maxFunc(batches)
        minimum = self.minFunc(batches)
        average = self.averageFunc(batches)
        stDeviation = self.stdFunc(batches)
        firstP = self.firstPFunc(batches)
        secondP = self.secondPFunc(batches)
        thirdP = self.thirdPFunc(batches)
        fourthP = self.fourthPFunc(batches)
        
        return {
            "rfwId" : self.rfwId,
            "lastBatchId" : lastBatchId,
            "samples" : batches,
            "maximum" : maximum,
            "minimum" : minimum,
            "average" : average,
            "stDeviation" : stDeviation,
            "firstP" : firstP,
            "secondP": secondP,
            "thirdP" : thirdP,
            "fourthP" : fourthP
        }


#Protobuf response
    def binaryResult(self):
        samples = self.totalSamples()
        (batches, lastBatchId) = self.createBatches()
        maximum = self.maxFunc(batches)
        minimum = self.minFunc(batches)
        average = self.averageFunc(batches)
        stDeviation = self.stdFunc(batches)
        firstP = self.firstPFunc(batches)
        secondP = self.secondPFunc(batches)
        thirdP = self.thirdPFunc(batches)
        fourthP = self.fourthPFunc(batches)

        return {
            "rfwId" : self.rfwId,
            "lastBatchId" : lastBatchId,
            "totalSamples" : samples,
            "batches": batches,
            "maximum" : maximum,
            "minimum" : minimum,
            "average" : average,
            "stDeviation" : stDeviation,
            "firstP" : firstP,
            "secondP": secondP,
            "thirdP" : thirdP,
            "fourthP" : fourthP
        }


# Create batches
    def createBatches(self):
        batches = []
        column = self.columnCsv()
        lastBatchId = self.batchId
        for index in range(0, self.batchSize):
            batch = column[lastBatchId * self.batchUnit: (lastBatchId + 1) * self.batchUnit].to_dict()
            batches.append(batch)
            lastBatchId += 1
        

        return batches, (lastBatchId - 1)
        

# Create list of batches
    def convertToDict(self, batches):
        batchList = list()
        for batch in batches:
            dictBatch = batch
            batchList.append(dictBatch)
        return batchList


# Data analytics - maximum
    def maxFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return max(newList)


# Data analytics - mimimum
    def minFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return min(newList)


# Data analytics - average
    def averageFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return mean(newList)


# Data analytics - standard deviation
    def stdFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return statistics.stdev(newList)


# Data analytics - 10p 
    def firstPFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return np.percentile(newList,10)


# Data analytics - 50p 
    def secondPFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return np.percentile(newList,50)


# Data analytics - 95p 
    def thirdPFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return np.percentile(newList,95)


# Data analytics - 99p 
    def fourthPFunc(self, batches):
        newList = []
        for index in range(len(batches)):
            for key in batches[index]:
                number = batches[index][key]
                newList.append(number)
            index += 1

        return np.percentile(newList,99)


# Selecting column from csv file
    def columnCsv(self):
        column = self.csvData[self.workloadMetric]
        return column


# Calcultaing total number of samples
    def totalSamples(self):
        return self.batchSize * self.batchUnit
