from mastodon_client import MastodonClient 
import pytest

client = MastodonClient()
client.register_app('cs272app', 'https://mastodon.social')
client.authenticate_client()
client.log_in(input("Enter the OAuth authorization code: "))
client.initialize_user()

def test_posting():
    assert client.create_post("test") != None

def test_retrieving(self,id):
    assert client.get_post(id) != None


def test_deleting(id):
    assert client.create_post(id) != None
