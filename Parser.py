from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


class Parser:
    def __init__(self, htmlFile, csvFileName):
        self.htmlFile = htmlFile
        with open(htmlFile) as fp:
            co2soup = BeautifulSoup(fp, 'html.parser')
        self.htmlTable = co2soup.find('table')
        self.csvFile = open(csvFileName)

    def parseCsvFile(self):
        df = pd.read_csv(self.csvFile, skiprows=3)  # skip 3 rows of comments
        df = df.replace(np.nan, '', regex=True)  # replace Nan with blank
        yearCsvLists = df['year'].values.tolist()
        yearCsvLists = [int(i) for i in yearCsvLists]
        yearTopex = df['TOPEX/Poseidon'].values.tolist()
        yearTopex = [float(i) for i in yearTopex]
        return yearCsvLists, yearTopex

    def printTable(self):
        print(self.htmlTable)

    def tableHtml(self):
        htmlDataList = []
        table = self.htmlTable.find_all("td")
        for data in table:
            data.get('td')
            htmlDataList.append(data.text)
        return htmlDataList

    def organizeLists(self, htmlDataList):
        length = len(htmlDataList)
        yearList = htmlDataList[9:length:7]
        averageList = htmlDataList[12:length:7]

        # convert each list from string to correct data type
        yearList = [int(i) for i in yearList]
        averageList = [float(i) for i in averageList]

        return yearList, averageList
