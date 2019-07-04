from randomuser.models import User


class TestModel:
    def test_user_get_full_name(self, user_data):
        user = User(user_data)
        assert user.get_full_name() == "John Doe"

    def test_user_repr(self, user_data):
        user = User(user_data)
        assert user.__repr__() == "<RandomUser: 'John Doe'>"
