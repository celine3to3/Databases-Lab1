# Databases-Lab1

Carbon Emissions and Sea Level by Year

Uses Pandas and BS4 to read in the two data files:


Co2.html
<TBODY><TR><TD>2002</TD><TD>4</TD><TD>2002.292</TD>...
<TBODY><TR><TD>2002</TD><TD>5</TD><TD>2002.375</TD>...
<TBODY><TR><TD>2002</TD><TD>6</TD><TD>2002.458</TD>...


SeaLevel.csv

2002.3797,3.43000,1.23000,,
2002.4069,1.13000,0.33000,,
2002.4340,-5.67000,-2.17000,,

Both files have monthly/daily data.
Python iterators and reducers are used to handle converting data to annual.

Data is stored in a Pandas Dataframe after getting converted. Users can select a year to view the data for.


Database:

Stores the Dataframes in an SQLite data base.  Uses a class to interface to the SQLite database:

    class Database:
        def __init__(self):
            self.db = sqliteConnection()

            ...

Class has functionality for table creation, inserting, searching and deleting entries in the database.  


Program Output showing insertion, deletion, and accessing information by year

![lab1 output1](https://user-images.githubusercontent.com/121079918/210129432-0c14c651-2c92-483d-b63f-10649b699d96.png)

![lab1 output 2](https://user-images.githubusercontent.com/121079918/210129436-a7f69b42-5b2b-4963-880e-ec82db51f2fe.png)

![lab1 output 3](https://user-images.githubusercontent.com/121079918/210129434-b50a94b6-d1f3-4595-90ba-1b248342066f.png)

Database preview
**TOPEX/Poseidon Sea Level data begins at 1992
![lab1 database preview](https://user-images.githubusercontent.com/121079918/210161802-665118cf-7c28-441f-8783-45c66058d9ec.png)

