# University of Haripur GPA & CGPA Calculator
# Credit Hours Included

def marks_to_gpa(marks):
    if marks < 50:
        return 0.00
    elif marks == 50:
        return 1.00
    elif marks == 51:
        return 1.08
    elif marks == 52:
        return 1.17
    elif marks == 53:
        return 1.25
    elif marks == 54:
        return 1.33
    elif marks == 55:
        return 1.42
    elif marks == 56:
        return 1.50
    elif marks == 57:
        return 1.58
    elif marks == 58:
        return 1.67
    elif marks == 59:
        return 1.75
    elif marks == 60:
        return 1.83
    elif marks == 61:
        return 1.92
    elif marks == 62:
        return 2.00
    elif marks == 63:
        return 2.08
    elif marks == 64:
        return 2.17
    elif marks == 65:
        return 2.25
    elif marks == 66:
        return 2.33
    elif marks == 67:
        return 2.42
    elif marks == 68:
        return 2.50
    elif marks == 69:
        return 2.58
    elif marks == 70:
        return 2.67
    elif marks == 71:
        return 2.75
    elif marks == 72:
        return 2.83
    elif marks == 73:
        return 2.92
    elif marks == 74:
        return 3.00
    elif marks == 75:
        return 3.08
    elif marks == 76:
        return 3.17
    elif marks == 77:
        return 3.25
    elif marks == 78:
        return 3.33
    elif marks == 79:
        return 3.42
    elif marks == 80:
        return 3.50
    elif marks == 81:
        return 3.60
    elif marks == 82:
        return 3.70
    elif marks == 83:
        return 3.80
    elif marks == 84:
        return 3.90
    else:
        return 4.00


def calculate_gpa():
    subjects = int(input("Enter number of subjects: "))
    total_points = 0
    total_credits = 0

    for i in range(subjects):
        marks = int(input(f"Enter marks of subject {i+1}: "))
        credit = int(input(f"Enter credit hours of subject {i+1}: "))

        gpa = marks_to_gpa(marks)
        print(f"Subject {i+1} GPA: {gpa}")

        total_points += gpa * credit
        total_credits += credit

    semester_gpa = total_points / total_credits
    return round(semester_gpa, 2)


def calculate_cgpa():
    semesters = int(input("Enter number of semesters: "))
    total = 0

    for i in range(semesters):
        print(f"\n--- Semester {i+1} ---")
        gpa = calculate_gpa()
        print(f"Semester {i+1} GPA: {gpa}")
        total += gpa

    cgpa = total / semesters
    print("\n==========================")
    print("Final CGPA:", round(cgpa, 2))
    print("==========================")


# Main Program
print("University of Haripur")
print("Project : GPA and CGPA Calculator")
print("Name: Hassan Nawaz")
print("Roll No: F23-1206")
print("Department: Information Technology")
print("Program : Artificial Intelligence")
print("Instructor : Mam Zanaib Noor")
print(" ")

calculate_cgpa()