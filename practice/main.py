# Exercise 2: Medium - Student Grade Analyzer
# Objective: Practice nested loops, data processing, and working with multiple sequences.
# Problem:
# Create a comprehensive grade analysis system for a class of students. The program should process student data and generate detailed reports using various for loop techniques.
# Student Data Structure:
pythonstudents = [
    {"name": "Alice", "grades": [85, 92, 78, 96, 88]},
    {"name": "Bob", "grades": [76, 81, 72, 85, 79]},
    {"name": "Charlie", "grades": [95, 87, 91, 89, 93]},
    {"name": "Diana", "grades": [82, 88, 85, 90, 87]},
    {"name": "Eve", "grades": [91, 94, 89, 96, 92]}
]
# Program Requirements:

# Individual Student Reports:

# Calculate each student's average grade
# Find their highest and lowest grades
# Determine letter grade based on average
# Count grades above 90

total_averages = 0
grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
best_student = {"name": "", "average": 0}

subject_totals = [0,0,0,0,0]
honor_roll = []
needs_support = []
improving_students = []

print("INDIVIDUAL STUDENT REPORTS:")

for student in pythonstudents:
    grades = student["grades"]
    grade_greater_ninety = 0
    average = sum(grades) / 5
    highest_grade = max(grades)
    lowest_grade = min(grades)

    if average >= 90:
        alpha_grade = "A"
        honor_roll.append(student["name"])
    elif average >= 80:
        alpha_grade = "B"
    elif average >= 70:
        alpha_grade = "C"
    elif average >= 60:
        alpha_grade = "D"
    else:
        alpha_grade = "F"

    grade_distribution[alpha_grade] += 1

    if average < 80:
        needs_support.append(student["name"])

    for grade in grades:
        if grade > 90:
            grade_greater_ninety += 1

    for i in range(5):
        subject_totals[i] += grades[i]

    print(f'''
    =============================
    Student: {student["name"]}
    Grades: {grades}
    Average: {average}
    Highest: {highest_grade} | Lowest: {lowest_grade}
    Letter Grade: {alpha_grade}
    Grades above 90: {grade_greater_ninety}'''
    )

    total_averages += average

    if average > best_student["average"]:
        best_student = {"name": student["name"], "average": average}

    if sum(grades[-3:]) > sum(grades[:2]):
        improving_students.append(student["name"])


overall_class_average = total_averages/5 

print("\nCLASS STATISTICS:")
print("=================")
print(f"Overall Class Average: {overall_class_average}")
print(f"Best Performing Student: {best_student['name']} ({best_student['average']})")

print("\nGrade Distribution:")
for grade in ["A", "B", "C", "D", "F"]:
    print(f"{grade} grades: {grade_distribution[grade]} students")

print("\nSubject Averages:")
for i in range(5):
    subject_avg = subject_totals[i] / len(pythonstudents)
    print(f"Subject {i+1}: {subject_avg}")

print("\nSPECIAL RECOGNITION:")
print("====================")
print("Honor Roll (≥90 average):", ", ".join(honor_roll) if honor_roll else "None")
print("Students Showing Improvement:", ", ".join(improving_students) if improving_students else "None")
print("Students Needing Support (<80 average):", ", ".join(needs_support) if needs_support else "None")




# Class Statistics:

# Overall class average
# Best performing student
# Grade distribution (A, B, C, D, F counts)
# Subject-wise averages (assuming 5 subjects)


# Advanced Analysis:

# Students with improving trends (last 3 grades > first 2 grades average)
# Students needing help (average < 80)
# Honor roll students (average >= 90)



# Grading Scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

# Expected Output Format:
# === STUDENT GRADE ANALYZER ===

# INDIVIDUAL STUDENT REPORTS:
# =============================
# Student: Alice
# Grades: [85, 92, 78, 96, 88]
# Average: 87.8
# Highest: 96 | Lowest: 78
# Letter Grade: B
# Grades above 90: 2

# [Similar reports for each student...]

# CLASS STATISTICS:
# =================
# Overall Class Average: 86.4
# Best Performing Student: Charlie (91.0)

# Grade Distribution:
# A grades: 2 students
# B grades: 3 students
# C grades: 0 students
# D grades: 0 students
# F grades: 0 students

# Subject Averages:
# Subject 1: 85.8
# Subject 2: 88.4
# Subject 3: 83.0
# Subject 4: 91.2
# Subject 5: 85.8

# SPECIAL RECOGNITION:
# ====================
# Honor Roll (≥90 average): Charlie, Eve
# Students Showing Improvement: Alice, Bob
# Students Needing Support (<80 average): None