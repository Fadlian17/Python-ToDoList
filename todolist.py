import mysql.connector as mysql

config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'todopy'
}

connect = mysql.connect(**config)
c_cursor = connect.cursor()
# query_database = "create database todopy"
# c_cursor.execute(query_database)

# bikin table
query = "create table tb_todo (id INT PRIMARY KEY, name VARCHAR(20), activity VARCHAR(20), status BOOLEAN DEFAULT false)"
test = c_cursor.execute(query)

# show tables
show = "show tables"
test2 = c_cursor.execute(show)
for a in c_cursor:
    print(a)
