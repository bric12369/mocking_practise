from lib.track import *

def test_sets_title_and_artist_on_init():
    track1 = Track('Bring Me The Horizon', 'Sleepwalking')
    assert track1.artist == 'Bring Me The Horizon'
    assert track1.title == 'Sleepwalking'

def test_matches():
    track1 = Track('Bring Me The Horizon', 'Sleepwalking')
    assert track1.matches('Bring') == True
    assert track1.matches('he') == True
    assert track1.matches('Sleep') == True
    assert track1.matches('Not found') == False

def test_matches_ignores_case():
    track1 = Track('Bring Me The Horizon', 'Sleepwalking')    
    assert track1.matches('bring') == True
    assert track1.matches('HE') == True