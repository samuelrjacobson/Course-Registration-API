from course import Course, courses

class Student:
	def __init__(self, EID, name):
		self._EID = EID
		self._name = name
		self.registered_courses = []

	def addCourse(self, course):
		if course in courses:
			self.registered_courses.append(course)

	
registered_courses= []
students = []