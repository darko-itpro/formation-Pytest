
from project.home.status import heat_status

def test_status_hot():
    assert heat_status(25) == "Chaud"
