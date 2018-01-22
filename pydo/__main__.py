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

ARGUMENTS = startup(sys.argv[1:])
TASK_LIST = process_args(ARGUMENTS)
KEYS_OKAY = {
    '113' : 'q',
    '813' : 'q',
    '108' : 'l',
    '768' : 'l',
    '99' : 'c',
    '67' : 'c',
    '100' : 'd',
    '680' : 'd',
    '102' : 'f',
    '702' : 'f',
    str(curses.KEY_RESIZE) : curses.KEY_RESIZE
}

def main(stdscr):
    """main"""
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    max_pad_size = max_y - 6
    interactions.print_all_tasks(TASK_LIST, stdscr)
    while True:
        max_y, max_x = stdscr.getmaxyx()
        max_pad_size = max_y - 6
        int_input = interactions.get_intent(stdscr)
        usr_input = str(int_input)
        if usr_input in KEYS_OKAY or int_input == curses.KEY_RESIZE:
            usr_input = KEYS_OKAY[usr_input]
            interactions.action_loop(TASK_LIST, stdscr, usr_input, int_input)
        else:
            stdscr.addstr(max_y - 2, 0, "Invalid option: {}".format(usr_input), \
                 curses.color_pair(1))

curses.wrapper(main)
