import pytest
import sys
from project.home.status import heat_status

if sys.version_info >= (3, 8):
    pytest.skip("Demo for all", allow_module_level=True)

def test_status_hot():
    assert heat_status(25) == "Chaud", "Un truc qui va pas"

def test_status_cold():
    assert heat_status(10) == "Froid"

def test_status_good():
    assert heat_status(20) == "Bon"

def test_limit_cold():
    assert heat_status(18) == "Bon"

def test_limit_hot():
    assert heat_status(22) == "Bon"
