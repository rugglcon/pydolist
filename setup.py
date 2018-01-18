"""
setup.py

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

import setuptools

try:
    import pydo
except ImportError:
    print("pydo requires python 3.5 or greater. Exiting.")
    quit(1)

setuptools.setup(
    name='pydolist',
    version=pydo.config.__version__,
    author=pydo.config.AUTHOR,
    author_email=pydo.config.EMAIL,
    description='A simple terminal TODO app written in Python 3.',
    license="GPLv3",
    url=pydo.config.URL,
    packages=["pydo"],
    entry_points={"console_scripts": ["pydo=pydo.__main__:main"]},
    python_requires=">=3.5",
    zip_safe=False
)
