from mastodon_client import MastodonClient
import pytest
from unittest.mock import patch

client = MastodonClient()
client.register_app('cs272app', 'https://mastodon.social')
client.authenticate_client()
client.log_in(input("Enter the OAuth authorization code: "))
client.initialize_user()

#tests to creates a post with a unique id
@patch("mastodon_client.MastodonClient.create_post")
def test_posting(mock_create_post):
    mock_create_post.return_value = {"id": 11111, "content": "test"}
    assert client.create_post("test")["id"] == 11111

#test to get the post from the unique id
@patch("mastodon_client.MastodonClient.get_post")
def test_retrieving(mock_get_post):
    mock_get_post.return_value = {"id": 11111, "content": "test"}
    assert client.get_post(11111)["id"] == 11111

#test to see if the post gets deleted
@patch("mastodon_client.MastodonClient.delete_post")
def test_deleting(mock_delete_post):
    mock_delete_post.return_value = True
    assert client.delete_post(11111) is True

#test invalid retrieval
@patch("mastodon_client.MastodonClient.get_post")
def test_retrieving_invalid_post(mock_get_post):
    mock_get_post.return_value = None
    assert client.get_post(99999) is None

#test empty post wont be allowed
@patch("mastodon_client.MastodonClient.create_post")
def test_create_empty_post(mock_create_post):
    mock_create_post.return_value = None
    assert client.create_post("") is None