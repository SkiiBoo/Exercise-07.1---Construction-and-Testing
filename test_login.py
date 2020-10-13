import pytest
import System

username = 'calyam'
password =  '#yeet'

#pass
def test_login(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.__init__()
    if users[username]['role'] != 'professor':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem