from project.pyflix.media_utils import is_viewed

def test_media_is_viewed():
    media = {'title': 'Star Wars',
             'duration': 121,
             'viewed': True}
    assert is_viewed(media) is True


def test_media_is_not_viewed():
    media = {'title': 'Star Wars',
             'duration': 121,
             'viewed': False}
    assert is_viewed(media) is False
