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
import curses
import os
import sys
import threading
from time import sleep
from . import config
from . import utils
from . import interactions
from . import conf_parser

LIST_FILE = os.environ["HOME"] + "/.local/pydo/todo.json"
CONF_FILE = os.environ["HOME"] + "/.local/pydo/pydo.ini"
FILE_LOCK = threading.RLock()

def startup(args):
    """just prints a welcome message and gets arguments"""
    arguments = argparse.ArgumentParser(description="A simple terminal TODO app.")
    arguments.add_argument("-f", metavar="\"path/to/file\"", \
            help="Path to a list file named/placed differently than the default.")
    arguments.add_argument("-c", metavar="\"path/to/file\"", \
            help="Path to a conf file named/placed differently than the default.")
    arguments.add_argument("-v", action="store_true", \
            help="Prints version and license info of pydo.")
    return arguments.parse_args(args)

def process_args(args):
    """processes arguments"""
    list_dest = LIST_FILE
    conf_dest = CONF_FILE
    if args.f:
        print("An alternate list file was given: ", args.f)
        list_dest = args.f
    if args.c:
        print("An alternate conf file was given: ", args.c)
        conf_dest = args.c
    if args.v:
        print("pydo " + config.__version__)
        print("Copyright (C) 2018 Connor Ruggles")
        print("License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\n")
        print("This is free software: you are free to change and redistribute it.")
        print("There is NO WARRANTY, to the extent permitted by law.")
        sys.exit(0)
    conf_parser.parse_config(conf_dest)
    return utils.setup_list(list_dest, FILE_LOCK)

arguments = startup(sys.argv[1:])
task_list = process_args(arguments)

def main(stdscr):
    """main"""
    # utils.clear()
    print("\n+-----------------+")
    print("| Welcome to pydo |")
    print("+-----------------+\n")
    print("PyDo  Copyright (C) 2018  Connor Ruggles\n"
          "This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.\n"
          "This is free software, and you are welcome to redistribute it\n"
          "under certain conditions; refer to the License for details.\n")
    stdscr.clear()
    while True:
        usr_input = interactions.get_intent(stdscr)
        if usr_input == "l" or usr_input == "L":
            stdscr.clear()
            interactions.print_all_tasks(task_list, stdscr)
        elif usr_input == "c" or usr_input == "C":
            stdscr.clear()
            interactions.create_task(task_list, stdscr)
        elif usr_input == "d" or usr_input == "D":
            stdscr.clear()
            interactions.delete_task(task_list, stdscr)
        elif usr_input == "f" or usr_input == "F":
            stdscr.clear()
            interactions.finish_task(task_list, stdscr)
        elif usr_input == "q" or usr_input == "Q":
            stdscr.clear()
            stdscr.addstr(0, 1, "Waiting for sync to finish...")
            stdscr.refresh()
            # print("\nWaiting for sync to finish...")
            destroy_success = task_list.destroy()
            if destroy_success == 0:
                # print("Success")
                stdscr.addstr(1, 1, "Success")
                stdscr.refresh()
            elif destroy_success is None:
                pass
            else:
                # print("There was a problem syncing the file.")
                stdscr.addstr(1, 1, "There was a problem syncing the file.")
                stdscr.refresh()
            # print("Goodbye.")
            stdscr.addstr(2, 1, "Goodbye.")
            stdscr.refresh()
            sleep(2)
            sys.exit(0)
        else:
            # print("Invalid option.")
            stdscr.addstr(curses.LINES - 2, 6, "Invalid option.")

curses.wrapper(main)
