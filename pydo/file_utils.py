"""
contains all the utilities needed for remote file work

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

import subprocess
from .conf_parser import CONFIG

def send_remote(list_file):
    """syncs the remote task file with this one"""
    if "url" in CONFIG:
        with open("/dev/null", "w") as devnull:
            p_exit = subprocess.call(["scp", list_file, CONFIG["url"]["dest"]], stdout=devnull)
            devnull.close()
        return p_exit
    return None

def get_remote(list_file):
    """gets the remote task file"""
    if "url" in CONFIG:
        with open("/dev/null", "w") as devnull:
            p_exit = subprocess.call(["scp", CONFIG["url"]["dest"], list_file], stdout=devnull)
            devnull.close()
        return p_exit
    return None
