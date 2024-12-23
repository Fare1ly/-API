import requests
import pytest
from token_auth import get_token_auth


@pytest.fixture()
def token_auth():
    return get_token_auth()