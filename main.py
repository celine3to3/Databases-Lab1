import Parser
import Process
import Database


import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///Data.db')



def main():
    # set up files
    p = Parser.Parser('Co2.html', 'SeaLevel.csv')

    # parse carbon emissions file in lists
    htmlTableList = p.tableHtml()       # converts html table to a list of td data
    carbonColumnData = p.organizeLists(htmlTableList)    # 6 lists, 1 for each column

    # parse sea level csv into two lists
    csvColumnData = p.parseCsvFile()

    # process all data
    processor = Process.Process(carbonColumnData, csvColumnData)
    processor.calculateCo2UniqueYears()
    processor.calculateSeaLevelUniqueYears()
    processor.convertDataToAnnual()  # all data converted to annual

    # create data frames after data conversion
    co2DataFrame = processor.createHtmlDataFrame()
    csvDataFrame = processor.createCsvDataframe()

    # concat data frames
    carbonSeaLevelCombined = pd.concat([co2DataFrame, csvDataFrame], axis=1)
    carbonSeaLevelCombined = carbonSeaLevelCombined.reset_index(drop=True)

    # fixing index
    carbonSeaLevelCombined = carbonSeaLevelCombined.set_index('Year')
    # print(carbonSeaLevelCombined)

    # create database from combined dataframe
    db = Database.Database()
    db.importData(carbonSeaLevelCombined)

    print("Database display")
    db.display('Data')

    insert_query = """INSERT INTO Data (Year, CO2Average, TOPEX) VALUES (?, ?, ?)"""
    testYear = (2020, 425.642, 64.342)

    db.insert(insert_query, testYear)  # insert year
    print("After 2020 data inserted")
    db.display('Data')

    db.deleteRecord(2020)  # delete year
    print("After 2020 data deleted")
    db.display('Data')

    userInput = 1
    while userInput != 0:
        userInput = int(input("Enter the year to search for, or 0 to quit: "))
        if userInput == 0:
            print("Search ended")
            break
        db.searchYear(userInput)

main()
