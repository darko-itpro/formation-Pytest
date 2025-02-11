import pytest


@pytest.hookimpl()
def pytest_sessionstart(session):
    print("Hello from `pytest_sessionstart` hook!")


@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    print("Hello from `pytest_sessionfinish` hook!")
    print(f"Exit status: {exitstatus}")