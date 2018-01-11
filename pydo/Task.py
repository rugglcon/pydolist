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

    def get_description(self):
        """gets the description for this task"""
        return self.description

    def get_title(self):
        """gets the title for this task"""
        return self.title

    def finish(self):
        """sets this task to done"""
        self.done = True

    def is_done(self):
        """returns True if done, False otherwise"""
        return self.done

    def set_title(self, new_title):
        """sets the title of this task to the given title"""
        self.title = new_title

    def set_description(self, new_desc):
        """sets the description of this task to the given description"""
        self.description = new_desc
