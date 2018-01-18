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

import os
import sys
from .List import TaskList

def clear():
    """clears the screen"""
    _ = os.system('clear')

def setup_list(list_dest, file_lock):
    """sets up the todo list, which should be a json file"""
    check_file(list_dest)
    return TaskList(list_dest, file_lock)

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
