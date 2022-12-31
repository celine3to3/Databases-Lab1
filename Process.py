import pandas as pd
import numpy as np
import functools


class Process:
    def __init__(self, carbonEmissions, seaLevels):
        self.yearData = carbonEmissions[0]
        self.averageData = carbonEmissions[1]

        self.seaYearData = seaLevels[0]
        self.seaLevelData = seaLevels[1]
        self.uniqueSeaYears = []

    def calculateCo2UniqueYears(self):
        numYears = 0
        uniqueYears = []
        for i in self.yearData:
            if i not in uniqueYears:
                numYears += 1
                uniqueYears.append(i)
        self.yearData = uniqueYears

    def calculateSeaLevelUniqueYears(self):
        numYears = 0
        uniqueYears = []
        for i in self.seaYearData:
            if i not in uniqueYears:
                numYears += 1
                uniqueYears.append(i)
        self.uniqueSeaYears = uniqueYears

    def convertDailyToAnnual(self):
        numDays = []
        for i in range(1992, 2020):
            count = self.seaYearData.count(i)  # count unique occurences of each day in a year
            numDays.append(count)

        seaLevelData = self.seaLevelData
        it = iter(seaLevelData)
        value_array = [[next(it) for _ in range(days)] for days in numDays]
        summation = map(lambda lis: functools.reduce(lambda a, b: a + b, lis), value_array)

        return [round(i / j, 3) for i, j in zip(summation, numDays)]

    def monthlyToAnnual(self, dataList):
        # create an array and fill it with arrays that section part of the dataList
        # i = 0, dataList[0:12], i = 1, dataList[12:24], etc. until yearData ends, extracting monthly data for each year
        value_array = [dataList[i * 12:i * 12 + 12] for i in range(0, len(self.yearData))]

        # map changes lists of monthly values to lists of single annual avg values
        summation = map(lambda lis: functools.reduce(lambda a, b: a+b, lis), value_array)
        months_count = [len(val) for val in value_array]

        # returns a list of i/j, for i in summation and j in months_count
        return [round(i / j, 3) for i, j in zip(summation, months_count)]

    def convertDataToAnnual(self):
        self.averageData = self.monthlyToAnnual(self.averageData)
        self.seaLevelData = self.convertDailyToAnnual()

    def createHtmlDataFrame(self):
        data = {'Year': self.yearData, 'CO2Average': self.averageData}
        df = pd.DataFrame(data)
        return df

    def createCsvDataframe(self):
        # offset with nan, seaLevelData starts at 1992 while carbon starts at 1959
        nanList = [np.nan for i in range(0, 33)]

        # adjust data so sea levels start at 1992
        seaLevelDataAdjusted = nanList + self.seaLevelData

        df = pd.Series(seaLevelDataAdjusted, name='TOPEX')
        df = df.replace(np.nan, '', regex=True)  # replace Nan with blank
        return df
