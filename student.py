from course import Course, courses

class Student:
	def __init__(self, EID, name):
		self._EID = EID
		self._name = name
		self.registered_courses = []

	def addCourse(self, prefix, cn):
		for course in courses:
			if(course._prefix == prefix and course._course_number == cn):
				self.registered_courses.append(course)

	def confirmation(self):
		return
	
registered_courses= []
students = []