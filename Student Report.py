# Custom exception for negative marks
class NegativeMarksError(Exception):
    pass

# Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def get_valid_mark(self, subject_name):
        while True:
            try:
                mark = int(input(f"Enter marks for {subject_name}: "))
                if mark < 0:
                    raise NegativeMarksError("Marks cannot be negative.")
                return mark
            except ValueError:
                print("Please enter a number.")
            except NegativeMarksError as e:
                print(e)

    def input_marks(self):
        for subject in ["Math", "Science", "English"]:
            self.subjects[subject] = self.get_valid_mark(subject)

    def calculate_total(self):
        return sum(self.subjects.values())

    def calculate_average(self):
        return self.calculate_total() / len(self.subjects)

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

    def show_report(self):
        total = self.calculate_total()
        average = self.calculate_average()
        grade = self.calculate_grade()

        print("\n--- Student Report ---")
        print("Name:", self.name)
        for subject, mark in self.subjects.items():
            print(f"{subject}: {mark}")
        print("Total:", total)
        print("Average:", round(average, 2))
        print("Grade:", grade)


# Run the program
name = input("Enter student name: ")
student1 = Student(name)
student1.input_marks()
student1.show_report()