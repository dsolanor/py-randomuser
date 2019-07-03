import pytest
import randomuser
from randomuser.models import User


def test_get_one_user():
    user = randomuser.get()
    assert isinstance(user, User)
    assert isinstance(user.name_first, str)


def test_get_list_users():
    users = randomuser.get(results=10)
    assert isinstance(users, list)
    assert len(users) is 10
    assert isinstance(users[0].name_first, str)
