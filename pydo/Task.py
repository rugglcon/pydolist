"""
A class that holds data about an individual task.
"""
class Task:
    """
    A class that holds data about an individual task.
    """
    def __init__(self, title: str, description: str, done=False):
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

    def set_title(self, new_title: str):
        """sets the title of this task to the given title"""
        self.title = new_title

    def set_description(self, new_desc: str):
        """sets the description of this task to the given description"""
        self.description = new_desc
