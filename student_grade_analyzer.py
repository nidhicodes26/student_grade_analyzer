def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

highest = max(marks)
lowest = min(marks)

print("\n----- RESULT -----")
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

with open("report.txt", "w") as file:
    file.write("Student Grade Report\n")
    file.write("-------------------\n")

    for i, mark in enumerate(marks):
        grade = calculate_grade(mark)

        line = f"Student {i+1}: Marks={mark}, Grade={grade}\n"

        print(line)
        file.write(line)

print("\nReport saved successfully.")