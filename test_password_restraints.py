import pytest

username = 'yoooooooooooooooooooooooooboiiiiiiiiiiiiiiiii'
password =  'iKewlbrooooo0oooo0ooo27'

#pass
def test_password_restraints():
    if len(password) >= 20:
        assert False
