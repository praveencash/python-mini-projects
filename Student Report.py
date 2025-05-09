class NegativeMarksError(Exception):
    pass


def get_valid_mark(subject_name):
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


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


def show_student_report():
    name = input("Enter student name: ")
    s1 = get_valid_mark("Math")
    s2 = get_valid_mark("Science")
    s3 = get_valid_mark("English")

    total = s1 + s2 + s3
    average = total / 3
    grade = calculate_grade(average)

    print("\n--- Student Report ---")
    print("Name:", name)
    print("Math:", s1)
    print("Science:", s2)
    print("English:", s3)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)


# Run the report
show_student_report()