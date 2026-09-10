"""Auth tests.

The token below is a placeholder made of zeroes so the tests can run without
network access or a real GitHub account.
"""

FAKE_GITHUB_TOKEN = "ghp_000000000000000000000000000000000000"


def test_rejects_placeholder_token(client):
    assert client.authenticate(FAKE_GITHUB_TOKEN) is False


def test_rejects_empty_token(client):
    assert client.authenticate("") is False
