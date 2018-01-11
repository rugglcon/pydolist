# Contributing to PyDo

There's not many rules, but there's a teeny tiny little style guide:

## Style Guide
1. Please use 4 spaces for indentation, and write function-oriented code. If you're adding a class, please make them in their own file and make sure to import them in both \_\_init\_\_.py AND \_\_main\_\_.py.
2. Be sure to add the GPLv3 file header to all new files. Just copy the one at the top of \_\_main\_\_.py and paste it at the top of the new file underneath the module description, if there is one.
3. If there's any (semi) confusing lines of code, please leave a 1-2 line comment explaining what it does for documentation purposes.
4. Add a docstring to every new module and function you create.

## Submitting Issues
This is simple; just explain what your issue is, what OS you're running, and the `Traceback` you get if there is one, otherwise if it's a bug with the program itself describe the expected behavior and then the actual behavior. Issues should be formatted like this:

* __OS:__ Whatever OS you're running (e.g., Linux distro, Windows 7/10, MacOS 10.x).
* __Issue:__ Describe the actual issue here, and reference relevant points in the Traceback/actual behavior sections.
* __Traceback:__ if there is one, just paste the `Traceback`
* __Expected Behavior:__ Write what the program _should_ be doing (or what you think it should be doing).
* __Actual Behavior:__ Write what the program _actually_ does.

## Pull Requests
Just a few steps for this:

1. Fork this repo
2. Hack away and smash bugs
3. Submit a pull request with these constraints:
    * reference an existing issue if it fixes one
    * only submit a PR with one commit; if there's more than one, just go ahead and close the current PR and open a new one with the squashed commits
    * if it doesn't fix an existing issue, explain what is fixed

That's it! If you have any questions, feel free to email me at [conruggles@gmail.com](mailto:conruggles@gmail.com)