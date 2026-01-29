from lib.music_library import *
from unittest.mock import Mock

def test_adds_tracks_to_tracks_property():
    track1 = Mock()
    track2 = Mock()
    playlist = MusicLibrary()
    playlist.add(track1)
    playlist.add(track2)
    assert playlist.tracks == [track1, track2]

def test_search():
    track1_match = Mock()
    track1_match.matches.return_value = True
    track2_no_match = Mock()
    track2_no_match.matches.return_value = False
    playlist = MusicLibrary()
    playlist.add(track1_match)
    playlist.add(track2_no_match)
    assert playlist.search('keystring') == [track1_match]
