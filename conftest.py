import pytest

from fixture.ui import Ui, Headless


@pytest.fixture(scope="session")
def app(request):
    fixture = Ui()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def ghost(request):
    fixture = Headless()
    request.addfinalizer(fixture.destroy)
    return fixture