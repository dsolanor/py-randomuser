class User(object):
    def __init__(self, user_json_data):
        self.__dict__ = user_json_data

    @property
    def first_name(self):
        return self.name.get("first")

    @property
    def last_name(self):
        return self.name.get("last")

    @property
    def full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __repr__(self):
        return self.full_name
