# Student Grade Calculator (PS 20)

## 1. Project Overview
The Student Grade Calculator is a beginner-friendly Python command-line application. It asks for a student's name and marks in five subjects, then calculates the total marks, percentage, grade, and pass/fail result.

## 2. What the Project Does
- Accepts a student's name.
- Accepts marks for five subjects.
- Validates that each mark is numeric and between 0 and 100.
- Calculates the total marks and percentage.
- Assigns a grade based on the percentage.
- Displays whether the student passed or failed.
- Lets the user process multiple students in one run.

## 3. Grading Rules
| Percentage | Grade |
|---|---|
| 85% and above | A |
| 70% to below 85% | B |
| 55% to below 70% | C |
| 40% to below 55% | D |
| Below 40% | F |

The program reports **Pass** when the percentage is at least 40%; otherwise, it reports **Fail**.

## 4. Technologies Used
- **Python 3** — programming language used to implement the application.
- **Python built-in functions and features** — `input()`, `print()`, `float()`, `sum()`, `range()`, f-strings, lists, loops, conditional statements, and functions.
- **Exception handling** — `try/except ValueError` prevents invalid text input from crashing mark entry.
- **Command-line interface (CLI)** — the program runs in a terminal or console.

No external libraries, database, web framework, or API are used by the current version.

## 5. How It Is Built
The project is organized into small functions, each with a specific responsibility:

1. `read_marks(subject_no)` asks for a mark and repeats the prompt until the input is a number from 0 to 100.
2. `calculate_total(marks_list)` adds the marks using `sum()`.
3. `calculate_percentage(total, subjects=NUM_SUBJECTS)` calculates the percentage out of 500 total possible marks.
4. `find_grade(percentage)` maps the percentage to a grade using `if/elif/else`.
5. `find_result(percentage)` returns `Pass` or `Fail` using the 40% threshold.
6. `process_student()` collects the student's name and five marks, calls the calculation functions, and prints the result.
7. `ask_another()` asks whether another student's result should be calculated.
8. `main()` starts the application and repeats the process until the user chooses to stop.

The constants `NUM_SUBJECTS = 5` and `PASS_PERCENTAGE = 40` keep the subject count and passing threshold easy to change.

## 6. How to Run
1. Install Python 3 if it is not already installed.
2. Save `student_grade_calculator.py` and `README.md` in the same folder.
3. Open a terminal or command prompt in that folder.
4. Run:

   ```bash
   python student_grade_calculator.py
   ```

   On some systems, use:

   ```bash
   python3 student_grade_calculator.py
   ```

5. Enter the student's name and marks for subjects 1–5. Follow the prompts to calculate another student's result or exit.

## 7. Example
```text
=== Student Grade Calculator ===
Enter student name: Riya
Marks for subject 1: 90
Marks for subject 2: 80
Marks for subject 3: 75
Marks for subject 4: 85
Marks for subject 5: 70
Riya | Total: 400 | Percentage: 80.00% | Grade: B | Result: Pass
Another student? (y/n): n
Goodbye!
```

## 8. Input Validation
- Empty student names are rejected by asking again.
- Non-numeric marks are rejected.
- Marks below 0 or above 100 are rejected.
- The repeat prompt accepts `y`, `yes`, `n`, or `no` (case-insensitive).

## 9. Limitations
- The application works in the terminal; it does not have a graphical interface or website.
- It handles five subjects, each out of 100, in the current version.
- Results are displayed on screen and are not saved to a file or database.
- The pass/fail rule checks the overall percentage only; it does not separately check whether each subject has been passed.

## 10. Possible Future Improvements
- Add a graphical interface or web interface.
- Save student results to CSV or a database.
- Allow users to configure subjects and grading rules.
- Generate printable report cards.
- Add separate pass/fail checks for each subject.

## 11. Project Summary
This project demonstrates Python fundamentals, including functions, lists, loops, conditions, input validation, exception handling, and basic arithmetic. It is suitable as an introductory programming project.
