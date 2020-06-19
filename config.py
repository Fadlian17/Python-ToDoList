import mysql.connector as mysql
config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'mdd'
}
connect = mysql.connect(**config)
cursor = connect.cursor()
# bikin db
# query_database = "create database mdd"
# cursor.execute(query_database)
# nampilin db
query = "show databases"
test = cursor.execute(query)
for db in cursor:
    print(db)
# bikin table
# query = "create table product (id INT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10,2))"
# test = cursor.execute(query)
# # show tables
# show = "show tables"
# test2 = cursor.execute(show)
# for a in cursor:
#     print(a)
# insert table product
# query_insert = "INSERT INTO product""(id, name, price)""values (%(id)s,%(name)s,%(price)s)"
# val = {
#     'id' : '2',
#     'name' : 'taro',
#     'price' : 19000
# }
# cursor.execute(query_insert,val)
# connect.commit()
# select from product
# query_select = "select * from product"
# cursor.execute(query_select)
# for a in cursor:
#     print(a)
