import pytest
import System
import Student


stuName = 'akend3'
password = '123454321'

submission_date = '10/13/20'
due_date = '10/14/20'

#pass
def test_check_ontime(grading_system):
    users = grading_system.users
    grading_system.login(stuName,password)
    grading_system.usr.check_ontime(submission_date,due_date)
    grading_system.__init__()
    if submission_date != due_date:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem