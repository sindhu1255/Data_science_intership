
# Student Grade Calculator

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)

