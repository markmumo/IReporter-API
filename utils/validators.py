import re


class Validate:

    def is_string(self, name):
        return re.match("^[A-Za-z]{4,}$", name)
