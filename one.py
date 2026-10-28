NUM_SUBJECTS = 5
PASS_PERCENTAGE = 40


def read_marks(subject_no):

    while True:
        text = input(f"Marks for subject {subject_no}: ").strip()
        try:
            marks = float(text)
        except ValueError:
            print("Invalid marks. Enter a number between 0 and 100.")
            continue
        if 0 <= marks <= 100:
            return marks
        print("Invalid marks. Enter a number between 0 and 100.")


def calculate_total(marks_list):

    return sum(marks_list)


def calculate_percentage(total, subjects=NUM_SUBJECTS):
    
    return total / (subjects * 100) * 100


def find_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def find_result(percentage):
    if percentage >= PASS_PERCENTAGE:
        return "Pass"
    else:
        return "Fail"


def process_student():
    name = ""
    while not name:
        name = input("Enter student name: ").strip()
    marks = [read_marks(i) for i in range(1, NUM_SUBJECTS + 1)]
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = find_grade(percentage)
    result = find_result(percentage)
    print(f"{name} | Total: {total:g} | Percentage: {percentage:.2f}% "
          f"| Grade: {grade} | Result: {result}")


def ask_another():
    while True:
        answer = input("Another student? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print("=== Student Grade Calculator ===")
    while True:
        process_student()
        if not ask_another():
            break
    print("Goodbye!")


if __name__ == "__main__":
    main()