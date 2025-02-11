import pytest

@pytest.mark.device(id="eu1235")
def test_device_eu():
    assert True

@pytest.mark.device(id="eu1235")
def test_device_other_case_eu():
    assert True

@pytest.mark.device(id="us142")
def test_device_us():
    assert True