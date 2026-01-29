from lib.track import *
from lib.music_library import *

def test_adds_tracks_to_tracks_property():
    track1 = Track('Bring Me The Horizon', 'Sleepwalking')
    track2 = Track('Biffy Clyro', 'Space')
    playlist = MusicLibrary()
    playlist.add(track1)
    playlist.add(track2)
    assert playlist.tracks == [track1, track2]

def test_search():
    track1 = Track('Bring Me The Horizon', 'Sleepwalking')
    track2 = Track('Biffy Clyro', 'Space')
    playlist = MusicLibrary()
    playlist.add(track1)
    playlist.add(track2)
    assert playlist.search('B') == [track1, track2]   
    assert playlist.search('Biffy') == [track2]
    assert playlist.search('Not found') == []