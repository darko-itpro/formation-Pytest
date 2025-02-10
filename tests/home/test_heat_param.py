import pytest
from project.home.status import heat_status

test_data = [
    (25, "Chaud"),
    pytest.param(18, "Froid", marks=pytest.mark.skip("Attente spec #7967")),
    (10, "Froid"),
]

@pytest.mark.parametrize("temperature, expected", test_data)
def test_status_good(temperature, expected):
    assert heat_status(temperature) == expected
