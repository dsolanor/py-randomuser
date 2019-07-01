import requests
import urllib.parse
from .models import User as UserModel

BASE_URL = "https://randomuser.me"
USER_PATH = "/api"
USERS_PATH = "/api/?results={}"


class ApiClient(object):
    def __init__(self, base_url):
        self._base_url = base_url

    @property
    def base_url(self):
        return self._base_url

    def get(self, path, **kwargs):
        if kwargs:
            kwargs_to_url = urllib.parse.urlencode(kwargs)
            path = f'{path}&{kwargs_to_url}'
        url = urllib.parse.urljoin(self.base_url, path, kwargs)
        res = requests.get(url)
        print(url)
        return res


class Base(object):
    def __init__(self, base_url, path):
        self._api = ApiClient(base_url)
        self._path = path

    def get(self, **kwargs):
        res = self._api.get(self._path, **kwargs)
        return res


class User(Base):
    def __init__(self):
        super().__init__(BASE_URL, USER_PATH)

    def get(self, **kwargs):
        res = super().get(**kwargs)
        user_json_data = res.json().get("results")[0]
        return UserModel(user_json_data)


class Users(Base):
    def __init__(self, num_users=10):
        path = USERS_PATH.format(num_users)
        self._users = []
        super().__init__(BASE_URL, path)

    def get(self, **kwargs):
        res = super().get(**kwargs)
        users_json_data = res.json().get("results")
        self._users = [UserModel(r) for r in users_json_data]
        return self._users

    @property
    def users(self):
        return self._users

    def __getitem__(self, item):
        return self.users[item]

    def __len__(self):
        return len(self._users)

    def __iter__(self):
        return iter(self._users)

    def __repr__(self):
        return f"{self.users}"


def get(results=1, **kwargs):
    if results <= 1:
        return User(**kwargs).get()
    else:
        return Users(num_users=results).get(**kwargs)
