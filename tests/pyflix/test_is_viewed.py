import pytest
from project.pyflix.media_utils import is_viewed

test_data = [({'title': 'Star Wars',
               'duration': 121,
               'viewed': True}, True),

             ({'title': 'Star Wars',
               'duration': 121,
               'viewed': False}, False),

             ({'title': 'Star Wars: Episode I - The Phantom Menace',
               'duration': 136,
               'viewed': 0}, False)]

@pytest.mark.parametrize("media, expected", test_data)
def test_is_viewed(media, expected):
    assert is_viewed(media) is expected
