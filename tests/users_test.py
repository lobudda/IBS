import requests
import pytest

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from configuration import BASE_URL as base_url
from src.enums.global_enums import GlobalErrorMessages


@pytest.fixture
def new_user_payload():
    return {
        "name": "morpheus",
        "job": "leader"
    }

@pytest.fixture
def existing_user_payload():
    return {
        "name": "morpheus",
        "job": "zion resident"
    }

@pytest.fixture
def create_user():
    payload = new_user_payload()
    response = requests.post(f"{base_url}/users", json=payload)
    assert response.status_code == 201
    return response.json()

class Test_Users():
    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_get_single_user(self, user_id):
        response = requests.get(f"{base_url}/users/{user_id}")
        assert response.status_code == 200, GlobalErrorMessages.ERROR_STATUS_CODE.value
        assert response.json()['data']['id'] == user_id
    def test_get_users_list(self):
        response = requests.get(f"{base_url}/users?page=2")
        assert response.status_code == 200, GlobalErrorMessages.ERROR_STATUS_CODE.value
        assert len(response.json()['data']) > 0

    def test_create_user(self, new_user_payload):
        response = requests.post(f"{base_url}/users", json=new_user_payload)
        assert response.status_code == 201, GlobalErrorMessages.ERROR_STATUS_CODE.value
        assert response.json()['name'] == new_user_payload['name']
        assert response.json()['job'] == new_user_payload['job']

    def test_update_user(self, existing_user_payload):
        response = requests.put(f"{base_url}/users/2", json=existing_user_payload)
        assert response.status_code == 200, GlobalErrorMessages.ERROR_STATUS_CODE.value
        assert response.json()['job'] == existing_user_payload['job']

    def test_delete_user(self):
        response = requests.delete(f"{base_url}/users/2")
        assert response.status_code == 204, GlobalErrorMessages.ERROR_STATUS_CODE.value

    def test_user_not_found(self):
        response = requests.get(f"{base_url}/unknown/100")
        assert response.status_code == 404, GlobalErrorMessages.ERROR_STATUS_CODE.value
        assert 'data' not in response.json()

