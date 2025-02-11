from pathlib import Path
import pytest

@pytest.fixture
def get_file(tmp_path):
    d = tmp_path / "asn"
    d.mkdir()
    p: Path = d / "asn.txt"
    p.write_text("Hello asn")

    yield p.read_text(encoding="utf-8")

    p.unlink()


@pytest.fixture
def get_old_file(tmp_path, request):
    d = tmp_path / "asn"
    d.mkdir()
    p: Path = d / "asn.txt"
    p.write_text("Hello asn")

    def delete_file():
        p.unlink()

    request.addfinalizer(delete_file)

    return p.read_text(encoding="utf-8")



def test_create_path(get_file):
    assert get_file == "Hello asn"
