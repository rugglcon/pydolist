"""
Copyright (C) 2018 Connor Ruggles

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from . import Task
from . import utils

def get_intent():
    """gets the intent of the user"""
    print("What would you like to do?\n")
    return input("(l)ist tasks; (c)reate task; (d)elete task; (f)inish task; (q)uit > ")

def print_all_tasks(list_object):
    """
    calls a function to retrieve all
    tasks, then prints them
    """
    utils.clear()
    print("All tasks:")
    print("----------")
    list_object.print_tasks()

def create_task(list_object):
    """
    creates a task with user input of
    title and description
    """
    utils.clear()
    print("New task")
    print("--------")
    title = input("Title of new task: ")
    desc = input("Description of new task (leave blank for no description): ")
    new_task = Task.Task(title, desc)
    list_object.add_task(new_task)
    print("New Task successfully created.\n")

def delete_task(list_object):
    """deletes the selected task"""
    utils.clear()
    print("Deleting task")
    print("-------------")
    list_object.print_tasks()
    index = input("Which task to delete? (1 for first task, 2 for second, etc.)\n> ")
    list_object.delete_task(int(index) - 1)

def finish_task(list_object):
    """finishes the selected task"""
    utils.clear()
    print("Finishing task")
    print("--------------")
    list_object.print_tasks()
    index = input("Which task to finish? (1 for first task, 2 for second, etc.)\n> ")
    list_object.finish_task(int(index) - 1)

def show_w():
    """prints the warranty section of GPL"""
    utils.clear()
    print("THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY\n"
          "APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT\n"
          "HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY\n"
          "OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,\n"
          "THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\n"
          "PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM\n"
          "IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF\n"
          "ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\n")
