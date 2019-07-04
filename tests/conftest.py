from pytest import fixture


@fixture(scope='session')
def user_data():
    user = {
        'name_first': 'john',
        'name_last': 'doe'
    }
    return user
