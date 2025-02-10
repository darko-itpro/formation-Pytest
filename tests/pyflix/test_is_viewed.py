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

def test_must_raise_on_negative_values():
    media = {'title': 'Star Wars: Episode I - The Phantom Menace',
               'duration': 136,
               'viewed': -1}

    with pytest.raises(ValueError):
        is_viewed(media)


#    with pytest.raises(LookupError) as exc:
#        is_viewed(media)
#    assert type(exc) == LookupError
