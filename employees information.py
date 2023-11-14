#database name=employee
# importing required library 
import mysql.connector 
# connecting to the database 
details=[] #details[0]=height #details[1]=weight
cnx= mysql.connector.connect(
                     host = "localhost",
                     user = "root",
                     passwd = "",
                     database = "employee" )  
cursorObject = cnx.cursor() 

