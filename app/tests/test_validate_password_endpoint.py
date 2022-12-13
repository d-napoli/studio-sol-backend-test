import pytest
from app.view_main import verify_password
import json


ENDPOINT = "0.0.0.0:8000/verify/"


def test_endpoint_only_accept_post_request(rf):
    request = rf.get(ENDPOINT)
    response = verify_password(request)
    assert response.status_code == 200


def test_password_without_min_size_returns_error(rf):
    payload = {
        "password": "abc",
        "rules": [
            {"rule": "minSize", "value": 4},
        ],
    }

    request = rf.post(ENDPOINT, json.loads(payload))
    response = verify_password(request)

    assert response.status_code == 200


def test_password_without_min_special_chars_returns_error(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "minSpecialChars", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, json.loads(payload))
    response = verify_password(request)

    assert response.status_code == 200


def test_password_without_min_digits_returns_error(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "minDigit", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, json.loads(payload))
    response = verify_password(request)

    assert response.status_code == 200


def test_password_with_sequenced_repeated_chars_returns_error(rf):
    payload = {
        "password": "aabcd",
        "rules": [
            {"rule": "noRepeted", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, json.loads(payload))
    response = verify_password(request)

    assert response.status_code == 200


def test_password_without_sequenced_repeated_chars_doesnt_return_error(rf):
    payload = {
        "password": "aabcd",
        "rules": [
            {"rule": "noRepeted", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, json.loads(payload))
    response = verify_password(request)

    assert response.status_code == 200
