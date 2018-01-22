"""
A class that holds data about an individual task.

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

class Task:
    """
    A class that holds data about an individual task.
    """
    def __init__(self, title, description, done=False):
        self.title = title
        self.description = description
        self.done = done
        self.__dict__ = {
            "title": self.title,
            "description": self.description,
            "done": self.done,
        }

    def finish(self):
        """sets this task to done"""
        self.done = True
