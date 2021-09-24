import pytest


from api import API


@pytest.fixture
def api():
    """explaine here..."""
    return API()

@pytest.fixture
def client(api):
    """explaine here..."""
    return api.test_session()
