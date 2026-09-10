"""Tests for the GitHub client's token handling.

The token below is a fixture value used to exercise the rejection path. It
has never been a live credential.
"""

PLACEHOLDER_GITHUB_TOKEN = "ghp_R7kQ2mXvL9pD4wZnB6tYcF1sJgA3eU8hNiPr"


def test_rejects_unknown_token(client):
    assert client.authenticate(PLACEHOLDER_GITHUB_TOKEN) is False


def test_rejects_empty_token(client):
    assert client.authenticate("") is False
