import requests
import urllib.parse
from .models import User as UserModel
from abc import ABCMeta, abstractmethod

BASE_URL = "https://randomuser.me"
API_PATH = "/api/"


class ApiClient(object):
    _base_url = BASE_URL
    _api_path = API_PATH

    def get(self, **kwargs):
        kwargs_to_url = urllib.parse.urlencode(kwargs)
        path = f'{self._api_path}?{kwargs_to_url}' if kwargs_to_url else self._api_path

        url = urllib.parse.urljoin(self._base_url, path)
        return requests.get(url)


class Base(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._api = ApiClient()

    @abstractmethod
    def get(self, **kwargs):
        res = self._api.get(**kwargs)
        return res


class User(Base):
    def get(self, **kwargs):
        res = super().get(**kwargs)
        user_json_data = res.json().get("results")[0]
        return UserModel(user_json_data)


class Users(Base):
    def __init__(self):
        super().__init__()
        self._users = []

    def get(self, **kwargs):
        res = super().get(**kwargs)
        users_json_data = res.json().get("results")
        self._users = [UserModel(r) for r in users_json_data]
        return self._users

    def __getitem__(self, item):
        return self._users[item]

    def __len__(self):
        return len(self._users)

    def __iter__(self):
        return iter(self._users)

    def __repr__(self):
        return f"{self._users}"


def get(results=1, **kwargs):
    if results <= 1:
        return User().get(**kwargs)
    else:
        return Users().get(results=results, **kwargs)
