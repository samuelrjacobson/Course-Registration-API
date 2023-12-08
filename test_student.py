from course import Course, courses
from student import Student, registered_courses
import pytest

course = Course("COSC", "111", 30, "John Doe", 
        "Programming I", "PH 503", "TH 9:00")

@pytest.fixture
def student():
	student = Student("E01234567", "Claude Mill")
	return student

"""
def test_addCourse(student, mocker):
	mocker.patch(
		'student.Student.confirmation'
	)
	student.addCourse(course._prefix, course._course_number)
	assert student.registered_courses[0]._prefix == course._prefix and student.registered_courses[0]._course_number == course._course_number
	assert not student.registered_courses[0] == None
"""
def test_addCourse(student):
	courses.append(course)

	student.addCourse(course._prefix, course._course_number)
	assert student.registered_courses[0] == course
	assert not student.registered_courses.pop() == None
