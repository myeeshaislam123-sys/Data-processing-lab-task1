marks = [70, 55, 80, 45, 90]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = 0

for mark in marks:
    if mark >= 50:
        passed = passed + 1

print("Total Marks:", total)
print("Average Mark:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Passed Courses:", passed)
