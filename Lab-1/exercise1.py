name = input("Enter student name: ")

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))
m5 = float(input("Enter mark 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

highest = max(m1, m2, m3, m4, m5)
lowest = min(m1, m2, m3, m4, m5)

passed = 0

if m1 >= 50:
    passed += 1
if m2 >= 50:
    passed += 1
if m3 >= 50:
    passed += 1
if m4 >= 50:
    passed += 1
if m5 >= 50:
    passed += 1

if average >= 80:
    performance = "Excellent"
elif average >= 70:
    performance = "Good"
elif average >= 60:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("Student Report")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed Courses:", passed)
print("Performance:", performance)

