import pytest
import sys
from project.home.status import heat_status

skipsystem = pytest.mark.skipif(sys.platform == "linux", reason="not implemented")


def test_status_hot():
    assert heat_status(25) == "Chaud", "Un truc qui va pas"

def test_status_cold():
    assert heat_status(10) == "Froid"

@skipsystem
def test_status_good():
    assert heat_status(20) == "Bon"

@pytest.mark.skip(reason="Attente ticke #4564")
def test_limit_cold():
    assert heat_status(18) == "Bon"

@pytest.mark.skip(reason="Attente ticke #4564bis")
def test_limit_hot():
    assert heat_status(22) == "Bon"
