
class Course:
    def __init__(self, prefix, course_number, cap, instructor, name, place, meeting_times):
        self._prefix = prefix
        self._course_number = course_number
        self._cap = cap
        self._instructor = instructor
        self._name = name
        self._place = place
        self._meeting_times = meeting_times 

    def is_prefix(self, prefix):
        return self._prefix == prefix


courses = []
courseA = Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")
courses.append(courseA)