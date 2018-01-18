"""
parses the pydo.conf file

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

import configparser
import os
import sys

CONFIG = configparser.ConfigParser()

def parse_config(conf_dest):
    """parses the config file for pydo at the passed in location"""
    conf_dest = os.path.expanduser(conf_dest)
    if os.path.exists(conf_dest):
        if not os.path.isfile(conf_dest):
            print("pydo: Conf file needs to be a file.")
            sys.exit(1)
        CONFIG.read(conf_dest)
    else:
        print("pydo: File " + conf_dest + " doesn't exist. Not using config file.")
