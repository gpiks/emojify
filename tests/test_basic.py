from emojify import create_app

import pytest


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_hello(client):
    # GIVEN
    # WHEN
    response = client.post("/", json={"text": "Hello, World!"})
    # THEN
    assert response.data == b"Hello, World!"


def test_bad_request(client):
    # GIVEN
    # WHEN
    response = client.post("/", json={"not_text": "hello!"})
    # THEN
    assert b"Bad Request" in response.data


def test_get_basic(client):
    # GIVEN
    # WHEN
    response = client.get("/")
    # THEN
    assert b"Test successful!"
