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
from . import config
from . import utils
from . import interactions

LIST_FILE = os.environ["HOME"] + "/.local/pydo/todo.json"

def startup(args):
    """just prints a welcome message and gets arguments"""
    arguments = argparse.ArgumentParser(description="A simple terminal TODO app.")
    arguments.add_argument("-f", metavar="\"path/to/file\"", \
            help="Path to a file named/placed differently than the default.")
    arguments.add_argument("-v", action="store_true", \
            help="Prints version number of pydo.")
    return arguments.parse_args(args)

def process_args(args):
    """processes arguments"""
    list_dest = LIST_FILE
    if args.f:
        print("An alternate list file was given: ", args.f)
        list_dest = args.f
    if args.v:
        print("pydo " + config.__version__)
        sys.exit(0)
    return utils.setup_list(list_dest)

def main():
    """main"""
    arguments = startup(sys.argv[1:])
    task_list = process_args(arguments)
    utils.clear()
    print("\n+-----------------+")
    print("| Welcome to pydo |")
    print("+-----------------+\n")
    print("PyDo  Copyright (C) 2018  Connor Ruggles\n"
          "This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n"
          "This is free software, and you are welcome to redistribute it\n"
          "under certain conditions; refer to the License for details.\n")
    while True:
        usr_input = interactions.get_intent()
        if usr_input == "l" or usr_input == "L":
            interactions.print_all_tasks(task_list)
        elif usr_input == "c" or usr_input == "C":
            interactions.create_task(task_list)
        elif usr_input == "d" or usr_input == "D":
            interactions.delete_task(task_list)
        elif usr_input == "f" or usr_input == "F":
            interactions.finish_task(task_list)
        elif usr_input == "q" or usr_input == "Q":
            print("Goodbye.")
            sys.exit(0)
        elif usr_input == "show w":
            interactions.show_w()
        else:
            print("Invalid option.")

main()
