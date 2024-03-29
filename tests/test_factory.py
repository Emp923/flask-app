from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    responce = client.get('/hello')
    assert responce.data == b'Hello, World!'
