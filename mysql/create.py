import mysql.connector


def createTable():
    # establishing the connection
    db = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='2507')

    # Creating a cursor object using the cursor() method
    cur = db.cursor()

    # Dropping database weather if already exists.
    cur.execute("DROP database IF EXISTS WEATHERDB")

    # Creating a database
    sql = """CREATE DATABASE WEATHERDB"""
    cur.execute(sql)
    print("Database have been successfully created")

    # Retrieving the list of databases
    print("List of databases: ")
    cur.execute("SHOW DATABASES")
    print(cur.fetchall())

    # Closing the connection
    db.close()


if __name__ == '__main__':
    createTable()

