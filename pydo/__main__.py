"""
                       888
                       888
                       888
88888b.  888  888  .d88888  .d88b.
888 "88b 888  888 d88" 888 d88""88b
888  888 888  888 888  888 888  888
888 d88P Y88b 888 Y88b 888 Y88..88P
88888P"   "Y88888  "Y88888  "Y88P"
888           888
888      Y8b d88P
888       "Y88P"

A simple terminal TODO app written in Python 3.

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

import argparse
import os
import sys
from .List import TaskList
from . import Task
from . import config

LIST_FILE = os.environ["HOME"] + "/.local/pydo/todo.json"

def startup(args):
    """just prints a welcome message and gets arguments"""
    arguments = argparse.ArgumentParser(description="A simple terminal TODO app.")
    arguments.add_argument("-f", metavar="\"path/to/file\"", \
            help="Path to a file named/placed differently than the default.")
    arguments.add_argument("-v", action="store_true", \
            help="Prints version number of pydo.")
    return arguments.parse_args(args)

def clear():
    """clears the screen"""
    _ = os.system('clear')

def process_args(args):
    """processes arguments"""
    list_dest = LIST_FILE
    if args.f:
        print("An alternate list file was given: ", args.f)
        list_dest = args.f
    if args.v:
        print("pydo " + config.__version__)
        sys.exit(0)
    return setup_list(list_dest)

def setup_list(list_dest):
    """sets up the todo list, which should be a json file"""
    check_file(list_dest)
    return TaskList(list_dest)

def get_intent():
    """gets the intent of the user"""
    print("What would you like to do?\n")
    return input("(l)ist tasks; (c)reate task; (d)elete task; (f)inish task; (q)uit\n> ")

def print_all_tasks(list_object):
    """
    calls a function to retrieve all
    tasks, then prints them
    """
    clear()
    print("All tasks:")
    print("----------")
    list_object.print_tasks()

def create_task(list_object):
    """
    creates a task with user input of
    title and description
    """
    clear()
    print("New task")
    print("--------")
    title = input("Title of new task: ")
    desc = input("Description of new task (leave blank for no description): ")
    new_task = Task.Task(title, desc)
    list_object.add_task(new_task)
    print("New Task successfully created.\n")

def delete_task(list_object):
    """deletes the selected task"""
    clear()
    print("Deleting task")
    print("-------------")
    list_object.print_tasks()
    index = input("Which task to delete? (1 for first task, 2 for second, etc.)\n> ")
    list_object.delete_task(int(index) - 1)

def finish_task(list_object):
    """finishes the selected task"""
    clear()
    print("Finishing task")
    print("--------------")
    list_object.print_tasks()
    index = input("Which task to finish? (1 for first task, 2 for second, etc.)\n> ")
    list_object.finish_task(int(index) - 1)

def check_file(list_file):
    """checks for the existence of the todo list file"""
    list_file = os.path.expanduser(list_file)
    if os.path.exists(list_file):
        if not os.path.isfile(list_file):
            print("Arguments with '-f' need to be a file.")
            sys.exit(1)
        if os.path.splitext(list_file)[1] != ".json":
            print("File given must be a .json file.")
            sys.exit(1)
    else:
        os.makedirs(os.path.abspath(os.path.dirname(list_file)), exist_ok=True)
        with open(list_file, 'w+') as new_list:
            new_list.close()

def main():
    """main"""
    arguments = startup(sys.argv[1:])
    task_list = process_args(arguments)
    clear()
    print("\n+-----------------+")
    print("| Welcome to pydo |")
    print("+-----------------+\n")
    while True:
        usr_input = get_intent()
        if usr_input == "l" or usr_input == "L":
            print_all_tasks(task_list)
        elif usr_input == "c" or usr_input == "C":
            create_task(task_list)
        elif usr_input == "d" or usr_input == "D":
            delete_task(task_list)
        elif usr_input == "f" or usr_input == "F":
            finish_task(task_list)
        elif usr_input == "q" or usr_input == "Q":
            print("Goodbye.")
            sys.exit(0)
        else:
            print("Invalid option.")

main()
