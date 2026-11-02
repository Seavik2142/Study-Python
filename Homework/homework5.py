
class Student:
    def __init__(self, student_id, name, courses):
        self.student_id = student_id
        self.name = name
        self.courses = courses

    def __str__(self):
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}"
        )

    def __len__(self):
        return len(self.courses)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.student_id == other.student_id


student1 = Student(
    "S001",
    "Seavik",
    ["Python", "Database", "AI"]
)

student2 = Student(
    "S001",
    "Dara",
    ["Java", "Networking"]
)

print(student1)
print("Total Courses:", len(student1))

print("\nAre students equal?", student1 == student2)
print("Total Courses:", len(student2))
