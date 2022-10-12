import mysql.connector
import glob
import base64
 
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="backend_db"
)

tablename = "examples_table"

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def readBLOB(filefullname):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="backend_db"
        )

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT FileData from """ + tablename +""" where FileFullName = %s"""

        cursor.execute(sql_fetch_blob_query, (filefullname,))
        record = cursor.fetchall()
        for row in record:
            bioData = row[0]
            write_file(bioData,filefullname)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    readBLOB('adtte.json')