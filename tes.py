import click
import mysql.connector as mysql
config = {
    'host': '127.0.0.1',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'todo_db'
}
connect = mysql.connect(**config)
cursor = connect.cursor()


class Todo:
    def createDatabase():
        try:
            query_database = "CREATE DATABASE todo_db"
            print(query_database)
        except Exception as e:
            print(e)

    def createTable():
        try:
            create_table = "CREATE TABLE todo"
            print(create_table)
        except Exception as e:
            print(e)

    @click.group()
    def cliGroup():
        pass

    @cliGroup.command("list")
    def list():
        query = "SELECT * FROM todo"
        pointer = cursor.execute(query)
        for i in pointer:
            print(i)

    @cliGroup.command("add")
    @click.argument("new_todo", type=str)
    def add(new_todo):
        query_data = "INSERT INTO todo""(id, list)""VALUE (%(id)s, %(list)s, %(status)s)"
        emp_id = cursor.lastrowid
        last_status = cursor.
        new_todo_list = {
            'id': emp_id,
            'list': new_todo
        }
        cursor.execute(query_data, new_todo_list)
        connect.commit()

    @cliGroup.command("update")
    @click.argument("update_todo", type=str)
    def update(update_todo):
        query_data = "UPDATE todo SET""(list)"" = (%(list)s)"
        new_update = {
            'list': update_todo
        }
        cursor.execute(query_data, new_update)
        connect.commit()

    @cliGroup.command("del")
    @click.argument("id")
    def del(id):
        query_data = "DELETE FROM todo WHERE""(id)""= (%(id)s)"
        id = (id)
        cursor.execute(query_data, id)
        connect.commit()

    @cliGroup.command("clear")
    def clear():
        ask = input("Are you want to delete [y/n] ? ")
        query_data = "DELETE FROM todo"
        if ask == 'y':
            cursor.execute(query_data)
        else:
            pass
        connect.commit()

    @cliGroup.command("done")
    @click.argument('id')
    def done(id):
