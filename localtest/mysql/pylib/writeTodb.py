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

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    file.close()
    return binaryData

def insert_varibles_into_table(fullname, name, format, category, filepath):
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="backend_db"
        )
        mycursor = connection.cursor()
        mySql_insert_query = """INSERT INTO """ + tablename +""" (FileFullName, FileName, FileFormat, FileCategory,FileData) VALUES (%s, %s, %s, %s, %s) """

        jsondata = convertToBinaryData(filepath)
        # Convert data into tuple format
        insert_blob_tuple = (fullname, name, format, category, jsondata)
        result = mycursor.execute(mySql_insert_query, insert_blob_tuple)
        connection.commit()
        print("Record inserted successfully into "+tablename)

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            print("MySQL connection is closed")
            mycursor.close()
            connection.close()

if __name__ == "__main__":
    folderpath = '../../../resources/examples/'
    categories =['adam', 'i18n', 'sdtm']
    for cat in categories:
        path =  folderpath + cat + '/*'
        filelist = glob.glob(path)
        for oneit in filelist:
            onelist = str(oneit).split('/')
            filefullnamestr = onelist[-1]
            filenamelist = filefullnamestr.split('.')
            formatstr = filenamelist[1]
            filenamestr = filenamelist[0]
            base64_data = convertToBinaryData(oneit)
            insert_varibles_into_table(filefullnamestr, filenamestr, formatstr, cat, oneit)