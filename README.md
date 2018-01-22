# PyDo
A simple TODO app written in Python 3.

## Getting Started
For development and testing, fork this repository. No special python packages or modules are needed. To run PyDo, first follow the installation instructions, then do:
```
pydo

# for help, run this
pydo -h
```

### Prerequisites
All you will need to run PyDo is Python 3.

## Features
As the description says, PyDo is very simple. Currently, the features are:
* task storage in JSON format in `~/.local/pydo/todo.json`
* optional config file in `~/.local/pydo/pydo.ini`
* option to specify a different file to use to store lists at runtime (`-f` option)
* option to specify a different file to use as a config file at runtime (`-c` option)
* very simple curses interface; runs forever with prompt (see screenshots)
* show completion status of a task, in case a task is done but you don't want to delete it yet

### Config file format
The configuration file should be placed in `~/.local/pydo/pydo.ini` (or another location that is specified at runtime with the `-c` option) with the following format:
```
[url]
dest = user@serverip:/path/to/file.json
```

The program will retrieve this file upon startup if it exists, and send the local file to this destination if one is specified and the config file exists, all using `scp`. In order for this to work, it is required that you set up ssh key authentication with that server so as to not prompt a password input.

If you want this to work between multiple instances, you should make sure the config file is the same on all those instances.

## Wishlist
- [ ] TODO.txt support
- [ ] Dropbox support
- [x] synced instances of TODO lists (probably need some sort of server)
    * Syncs the entire TODO list file to a destination specified in a config file
- [ ] email reminders about tasks
- [x] switch interface to be entirely curses-based (started on branch `curses`)
- [ ] (extra wishlist) scan project source files for TODO comments and add them to the list

## Installing
```
# Installing system-wide with pip3:
sudo pip3 install pydolist

# Installing for your user:
pip3 install --user pydolist
# then add $HOME/.local/bin to your path
PATH="$PATH:$HOME/.local/bin"
```

### Manual Installation
Clone or download this repository then run:
```
# for system-wide use:
sudo pip3 install .

# user-only:
pip3 install --user .
# then add $HOME/.local/bin to your path
PATH="$PATH:$HOME/.local/bin"
```

## Screenshots
#### Welcome screen
![png](https://raw.githubusercontent.com/rugglcon/pydo/master/assets/welcome.png)

#### Listing all tasks
![png](https://raw.githubusercontent.com/rugglcon/pydo/master/assets/list.png)

## Contributing
Please read CONTRIBUTING.md for details on submitting pull requests and issues.

## Authors
* Connor Ruggles

## License
This project is licensed under the GNU GPLv3.0 OR ANY LATER VERSION - see LICENSE.md for details.