from service.app import App

import pytest # type: ignore



@pytest.fixture
def client():
    with App.test_client() as client:
        yield client

def test_hello(client):
    result = client.get('/')
    assert b'hello' in result.data