
from project.home.status import heat_status

def test_status_hot():
    assert heat_status(25) == "Chaud", "Un truc qui va pas"

def test_status_cold():
    assert heat_status(10) == "Froid"

def test_status_good():
    assert heat_status(20) == "Bon"