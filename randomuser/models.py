class User(object):
    name_first: str
    name_last: str
    cell: str
    dob_age: str
    dob_date: str
    email: str
    gender: str
    id_name: str
    id_value: str
    location_city: str
    location_coordinates_latitude: str
    location_coordinates_longitude: str
    location_postcode: str
    location_state: str
    location_street: str
    location_timezone_description: str
    location_timezone_offset: str
    login_md5: str
    login_password: str
    login_salt: str
    login_sha1: str
    login_sha256: str
    login_username: str
    login_uuid: str
    name_title: str
    nat: str
    phone: str
    picture_large: str
    picture_medium: str
    picture_thumbnail: str
    registered_age: str
    registered_date: str

    def __init__(self, user_json_data):
        self.__dict__ = self._flatten_json(user_json_data)

    def get_full_name(self):
        return f'{self.name_first.capitalize()} {self.name_last.capitalize()}'

    def __repr__(self):
        return '<RandomUser: \'{}\'>'.format(self.get_full_name())

    @staticmethod
    def _flatten_json(y):
        result = {}

        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            else:
                result[name[:-1]] = x

        flatten(y)
        return result

