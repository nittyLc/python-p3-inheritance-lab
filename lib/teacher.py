from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.students = []
        self.knowledge = ["Math", "Science", "History"]  # Example knowledge list

    def add_student(self, student):
        self.students.append(student)

    def teach(self):
        return self.knowledge[0]  # Example teaching method