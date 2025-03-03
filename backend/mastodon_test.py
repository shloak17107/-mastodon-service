from mastodon_client import MastodonClient 
import pytest

failed_client = MastodonClient()
def test_posting_error():
    with pytest.raises(ValueError):
        failed_client.create_post("test")

def test_retrieve_error():
    with pytest.raises(ValueError):
        failed_client.get_post("test")

def test_delete_error():
    with pytest.raises(ValueError):
        failed_client.delete_post("test")

client = MastodonClient()
client.register_app('cs272app', 'https://mastodon.social')
client.authenticate_client()
client.log_in(input("Enter the OAuth authorization code: "))
client.initialize_user()


def test_posting():
    assert client.create_post("test") != None


def test_retrieve(id):
    assert client.get_post(id) != None


def test_delete(id):
    assert client.delete_post(id) != None
