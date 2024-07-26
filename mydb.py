import pymysql


dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="Dilan@924"
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("All Done!")




