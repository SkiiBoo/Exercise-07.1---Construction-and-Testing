import pytest
import System
import Student


stuName = 'akend3'
password = '123454321'
assignment_name = 'assignment1'
submission = 'This is my submission, woo'
submission_date = '10/13/20'
courseName = 'comp_sci'

#pass
def test_submit_assignment(grading_system):
    users = grading_system.users
    grading_system.login(stuName,password)
    grading_system.usr.submit_assignment(courseName,assignment_name,submission,submission_date)
    grading_system.__init__()
    if users[stuName]['courses'][courseName][assignment_name]['submission'] == submission:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem