class student:
    _id_counter = 1

    def __init__(self, name):
        self.student_id = student._id_counter
        student._id_counter += 1

        self.name = name
        self.grades = {}
        self.enrolled_courses = []

    def __str__(self):
        return f"student id: {self.student_id}, NAME: {self.name}, Grades: {self.grades}"

    def __repr__(self):
        return f"student id: {self.student_id}, NAME: {self.name}, Grades: {self.grades}"
    def add_grade(self,course_id,grade):
        """
        this function helps the user to add specific grade to any course
        param_1 : takes grade 
        type param_1 :int
         param_2 : takes grade 
        type param_2 : take grade
        return : test 
        type_return : str
        """
        self.grades[course_id] = grade 
    def enrolled_courses(self,course):
        self.enrolled_courses.append()

 