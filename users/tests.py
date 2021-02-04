import requests


def test_first_api():
    keys = ('success', 'status_code', 'message')
    test_responce = requests.get(
        url='http://localhost:8000/users/test/',
    )
    assert tuple(test_responce.json().keys()) == keys
# Create your tests here.
