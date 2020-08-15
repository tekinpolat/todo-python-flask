import mysql.connector
from mysql.connector import Error


def dbconnect():
    try:
        conn = mysql.connector.connect(host='localhost', database='todo_flask', user='root', password='',auth_plugin='mysql_native_password')
        if conn.is_connected():
            print('Connected to MySQL database')
            
    except Error as e:
        print(e)
        
    return conn
    