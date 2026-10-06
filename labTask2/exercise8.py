students = [
    {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92},
    {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76},
    {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95},
    {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84},
    {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78}
]
def avg():
    total=0
    for i in students:
        total=total+i["marks"]
        avg=total/5
    print("avg:",avg)
def highest_marks():
    high=0
    highest_stu=" "
    for i in students:
        if i["marks"]>high:
            print("highest")
def count_lowAttendance():
    count=0
    for i in students:
        if i["attendance"]<80:
            count+=1
            print("low attendance")
avg()
highest_marks()
count_lowAttendance()

        
