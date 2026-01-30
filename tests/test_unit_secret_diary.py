from lib.secret_diary import *
from unittest.mock import Mock

def test_sets_diary_on_init():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert secret_diary.diary == diary

def test_sets_locked_to_true_on_init():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    assert secret_diary.locked == True  

def test_unlock_method():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.locked == False

def test_lock_method():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.locked == False
    secret_diary.lock()
    assert secret_diary.locked == True   

def test_read_method_locked():
    diary = Mock()
    diary.contents = 'These are my contents'
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == 'Go away!'

def test_read_method_unlocked():
    diary = Mock()
    diary.contents = 'These are my contents'
    diary.read.return_value = 'These are my contents'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'These are my contents'