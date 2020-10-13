import pytest

username = 'yoooooooooooooooooooooooooboiiiiiiiiiiiiiiiii'
password =  'iKewlbro'

#pass
def test_username_restraints():
    if len(username) >= 20:
        assert False