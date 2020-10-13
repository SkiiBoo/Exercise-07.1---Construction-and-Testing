import pytest
import System

username = 'calyam'
password =  '#yeet'

#pass
def test_check_password(grading_system):
    users = grading_system.users
    grading_system.check_password(username,password)
    grading_system.__init__()
    if users[username]['password'] == password:
        assert True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem