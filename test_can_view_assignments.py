import pytest
import System
import Student


stuName = 'akend3'
password = '123454321'
course = 'cloud_computing'

#pass
def test_can_view_assignments(grading_system):
    users = grading_system.users
    grading_system.login(stuName,password)
    
    courses = users[stuName]['courses']
    if course not in courses:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem