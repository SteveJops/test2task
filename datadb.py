# imports
import sqlite3 as sqlt
from pathlib import Path
import pandas as pd
from parsing import main


def insertData():
    """
    This func creates a database and adds all data from parsing.py
    script to currently created db or updated already created tables
    in the db with new info that was getting from the site
    :return: None
    """
    list_data = main()
    # Creating the database
    Path('weather.db').touch()
    print("Database has been successfully created ")

    # Connecting to db
    connect = sqlt.connect("weather.db")
    print("Establishing database...")

    # Creating a cursor object using the cursor() method
    cursor = connect.cursor()

    # Doping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS weather_data")

    # Creating the table with data
    sql = '''CREATE TABLE weather_data (DATE DATE, TEMP INT, DESCRIPT VARCHAR(255))'''
    print("Tables have been successfully created")
    cursor.execute(sql)

    try:
        # Preparing SQL query to INSERT a record into the database
        results = pd.DataFrame(list_data)
        results.to_sql('weather_data', connect, if_exists='append', index=False)
        connect.commit()

        # Fetching all the rows
        print("Contents of the Weather_data table: ")
        cursor.execute('''SELECT * from weather_data''')
        print(cursor.fetchall())

    except sqlt.Error as error:
        print('An error appears here:', error)
        # Rolling back in case of error
        connect.rollback()

    finally:

        print('Data has been successfully uploaded')
        # Finishing the current connection with db
        connect.close()


if __name__ == '__main__':
    insertData()
