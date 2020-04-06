class School:

    def __init__(self, courses, departments, professor, student):
        self.courses = courses
        self.departments = departments
        self.professor = professor
        self.student = student

    def printschool(self):
        print("The number of courses is:", self.courses)
        print("The number of department is:", self.departments)
        print("The number of professor in school are:", self.professor)
        print("The number of student in:", self.student)


class Schooltype(School):
    def __init__(self, courses, departments, professor, student, playground, library, typeschool):
        School.__init__(self, courses, departments, professor, student)
        self.playground = playground
        self.library = library
        self.typeschool = typeschool

    def printSchooltypedetail(self):
        self.printschool()
        print("Plaground is:", self.playground)
        print("library is:", self.library)
        print("Type of School is:", self.typeschool)


schooldetail = School("20", "10", "100", "1000")
schooldetail.printschool()

schooltypedetail = Schooltype("20", "10", "100", "1000", "small", "no library", "primary")
schooltypedetail.printSchooltypedetail()
