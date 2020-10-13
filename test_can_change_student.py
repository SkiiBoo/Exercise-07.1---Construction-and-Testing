import pytest
import System
import Professor

username = 'goggins'
password =  'augurrox'

stuName = 'smebmm'
courseName = 'cloud_computing'

#pass
def test_can_change_student(grading_system):
    courses = grading_system.courses
    grading_system.login(username,password)
    if courses[courseName]['professor'] != username:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem