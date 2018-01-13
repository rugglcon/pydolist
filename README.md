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
* task storage in JSON format in ~/.local/pydo/todo.json
* very simple interface; runs forever with prompt (see screenshots)
* show completion status of a task, in case a task is done but you don't want to delete it yet

## Wishlist
* TODO.txt support
* Dropbox support
* synced instances of TODO lists (probably need some sort of server)
* email reminders about tasks
* (extra wishlist) scan project source files for TODO comments and add them to the list

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