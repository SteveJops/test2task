from mysql.create import *


def createRows():
    # establishing the connection
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='2507',
        database='WEATHERDB')

    # Creating a cursor object using the cursor() method
    cur = db.cursor()

    # Dropping weather_data table if already exists.
    cur.execute("DROP TABLE IF EXISTS WEATHER_DATA")

    # Creating table as per requirement
    sql = '''CREATE TABLE WEATHER_DATA (DATE DATE, TEMP INT, DESCRIPT VARCHAR(255))'''

    cur.execute(sql)

    # Closing the connection
    db.close()


if __name__ == '__main__':
    createRows()
