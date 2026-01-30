from lib.diary import *

def test_sets_contents_on_init():
    diary = Diary('These are my contents')
    assert diary.contents == 'These are my contents'

def test_read_returns_contents():
    diary = Diary('These are my contents')
    assert diary.read() == 'These are my contents'    