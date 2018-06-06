import pytest
from falcon import testing
from rentomatic.app import create_app


# TODO : add test configuration
@pytest.yield_fixture()
def client():
    return testing.TestClient(create_app())
