import mysql.conndector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Latitude',
    
) 

#prepare the cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("all done")