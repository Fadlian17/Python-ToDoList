from datetime import datetime
import mysql.connector as mysql
import click

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
# query = "create table tb_todo (id INT PRIMARY KEY, name VARCHAR(20), activity VARCHAR(20), status BOOLEAN DEFAULT false)"
# test = c_cursor.execute(query)

# show tables
# show = "show tables"
# test2 = c_cursor.execute(show)
# for a in c_cursor:
#     print(a)


# """To Do List Programe"""
# """Represent a Tasks in the To-DoList.
# match against a string in searches and store each
# tasks"""
# last_id = 0


# class Task:
#     def __init__(self, task_name, complete=""):
#         self.task_name = task_name
#         self.complete = "N"
#         self.date_created = datetime.today().strftime('%d-%m-%y')
#         global last_id
#         last_id += 1
#         self.id = last_id

#     def match_task(self, filter):
#         """Determine if this note matches the filter
#         text. Return True if it matches, False otherwise.
#         Search is not case sensitive and matches any word in the tasks. """

#         return filter.lower() in self.task_name.lower()


# class ToDoList:
#     """Represent a collection of tasks that
#     can be searched, modified and complete and deleted """

#     def __init__(self):
#         self.tasks = []

#     def new_task(self, task_name, complete):
#         """Create new task and add it to the list"""
#         self.tasks.append(Task(task_name, complete))

#     def _find_task(self, task_id):
#         """locate the task with given id"""
#         for task_name in self.tasks:
#             if str(task_name.id) == str(task_name.id):
#                 return task_name
#         return None

#     def modify_task(self, task_id, task_name):
#         task_name = self._find_task(task_id)
#         if task_name:
#             task_name.task_name = task_name
#             return True
#         return False

#     def delete_task(self, task_id, complete):
#         task = self._find_task(task_id)
#         if task:
#             task.complete = "Y"
#             return self.tasks.remove(task_id-1)
#         return False

#     def search(self, filter):
#         """Find all task that match the given
#         fliter string """
#         return [task for task in self.tasks if task.match(filter)]

class Todolist:

    @click.group()
    def todo_app():
        pass

    @todo_app.command("show")
    @staticmethod
    def show():
        """Todopy List"""
        query = ("SELECT * FROM tb_todo")
        c_cursor.execute(query)
        for q in c_cursor:
            print(q)

    @todo_app.command("add")
    @click.argument("activity")
    def add(activity):
        """Todopy Add"""
        query_data = "INSERT INTO tb_todo (activity) VALUES (%s)"
        new_todo_list = (activity,)
        c_cursor.execute(query_data, new_todo_list)
        connect.commit()
        print("success add data todopy")

    @todo_app.command("update")
    @click.argument("id")
    @click.argument("activity")
    def update(id, activity):
        """Todopy Update"""
        query_data = "UPDATE tb_todo SET activity = (%s) WHERE id= (%s)"
        new_update = (activity, id)
        c_cursor.execute(query_data, new_update)
        connect.commit()
        print("success update todopy")

    @todo_app.command("delete")
    @click.argument("id")
    def delete(id):
        """Todopy Delete"""
        query_data = "DELETE FROM tb_todo WHERE id= (%s)"
        new_update = (id,)
        c_cursor.execute(query_data, new_update)
        connect.commit()
        print("success delete field todopy")

    @ todo_app.command("clear")
    def clear():
        """Todopy Clear"""
        ask_input = input("Are you want to delete ?")
        query_data = "DELETE FROM tb_todo"
        if ask_input == 'y':
            c_cursor.execute(query_data)
            connect.commit()

        print("success delete all field todopy")

    @ todo_app.command("done")
    @click.argument("id")
    def done(id):
        """Todopy DONE"""
        query_data = "UPDATE tb_todo SET status = 1 WHERE id= (%s)"
        new_update = (id,)
        all_data = c_cursor.execute(query_data, new_update)
        connect.commit()


if __name__ == '__main__':
    Todolist.todo_app()
