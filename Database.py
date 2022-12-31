import sqlite3
import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///Data.db')

class Database:
    global connection
    connection = sqlite3.connect('Data.db')

    def __init__(self):
        self.db = connection
        self.cursor = connection.cursor()
        self.database = ''

    def importData(self, dataframe):
        # dataframe gets imported into database
        # table name is Data
        self.database = dataframe.to_sql('Data', engine, if_exists='replace')
        return self.database

    def searchYear(self, year):
        global connection
        cursor = connection.cursor()

        sel = 'SELECT CO2Average FROM Data WHERE year == "{0}"'.format(year)
        cursor.execute(sel)
        co2Found = cursor.fetchone()

        sel = 'SELECT TOPEX FROM Data WHERE year == "{0}"'.format(year)
        cursor.execute(sel)
        seaLevelFound = cursor.fetchone()
        print("\n" + str(year) + " carbon emissions and sea level")
        print("Average CO2: ")
        [print(r) for r in co2Found]
        print("TOPEX/Poseidon:")
        [print(r) for r in seaLevelFound]

    def insert(self, query, tup):
        global connection
        try:
            cursor = connection.cursor()
            cursor.execute(query, tup)
            connection.commit()
            print("Inserted successfully")
        except sqlite3.Error as error:
            print("Failed to insert: ", error)

    def deleteRecord(self, year):
        global sqliteConnection
        try:
            cursor = connection.cursor()
            delete_query = "DELETE from Data where Year = " + str(year)
            cursor.execute(delete_query)
            connection.commit()
            print("Record deleted")
        except sqlite3.Error as error:
            print("Failed to delete record from Data table", error)

    def display(self, tableName):
        # convert current database to dataframe and display
        print(pd.read_sql(tableName, engine))

    def query_builder(self, operation):
        if operation == 'delete':
            print("DELETE from Data where column1 = value1")
            column1 = input("Input column1: ")
            value1 = input("Input value1: ")
            return "DELETE from Data where " + column1 + " = " + str(value1)
        elif operation == 'select':
            print("SELECT column1 FROM Data WHERE column2 == \"{0}\"\'.format(value1)")
            value1 = input("Input column1: ")
            value2 = input("Input column2: ")
            value3 = input("Input value1: ")
            return "SELECT " + value1 + " FROM Data WHERE " + value2 + " == \"{0}\"\'.format(" + value3 + ")"