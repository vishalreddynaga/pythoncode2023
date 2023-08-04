

import pyodbc as po
 
# Connection variables
server = 'localhost'
database = 'AdventureWorks2019'
username = 'sa'
password = 'root'
 
# Connection string
cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
        server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM table_name')

# for i in cursor:
#     print(i)