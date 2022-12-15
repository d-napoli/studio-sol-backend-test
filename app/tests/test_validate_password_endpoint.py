import pytest
import json

from app.view_main import verify_password

ENDPOINT = "/verify"


def test_endpoint_only_accept_post_request(rf):
    request = rf.get(ENDPOINT)
    response = verify_password(request)
    assert response.status_code == 405


def test_password_without_min_size_returns_no_match(rf):
    payload = {
        "password": "abc",
        "rules": [
            {"rule": "minSize", "value": 4},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == False
    assert len(response_content["noMatch"]) == 1
    assert response_content["noMatch"][0] == "minSize"


def test_password_with_min_size_is_okay(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "minSize", "value": 4},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == True
    assert len(response_content["noMatch"]) == 0


def test_password_without_min_special_chars_returns_error(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "minSpecialChars", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == False
    assert len(response_content["noMatch"]) == 1
    assert response_content["noMatch"][0] == "minSpecialChars"


def test_password_with_min_special_chars_is_okay(rf):
    payload = {
        "password": "abcd#",
        "rules": [
            {"rule": "minSpecialChars", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == True
    assert len(response_content["noMatch"]) == 0


def test_password_without_min_digits_returns_error(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "minDigit", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == False
    assert len(response_content["noMatch"]) == 1
    assert response_content["noMatch"][0] == "minDigit"


def test_password_with_min_digits_is_okay(rf):
    payload = {
        "password": "abcd1",
        "rules": [
            {"rule": "minDigit", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == True
    assert len(response_content["noMatch"]) == 0


def test_password_with_sequenced_repeated_chars_returns_error(rf):
    payload = {
        "password": "aabcd",
        "rules": [
            {"rule": "noRepeted", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == False
    assert len(response_content["noMatch"]) == 1
    assert response_content["noMatch"][0] == "noRepeted"


def test_password_without_sequenced_repeated_chars_is_okay(rf):
    payload = {
        "password": "abcd",
        "rules": [
            {"rule": "noRepeted", "value": 1},
        ],
    }

    request = rf.post(ENDPOINT, payload, content_type="application/json")
    response = verify_password(request)

    assert response.status_code == 200

    response_content = json.loads(response.content)

    assert response_content["verify"] == True
    assert len(response_content["noMatch"]) == 0
