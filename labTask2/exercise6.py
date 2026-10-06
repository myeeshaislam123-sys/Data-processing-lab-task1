marks=(50,60,40,80,90)
def calculate_grade(marks):
    avg=sum(marks)/5
    if avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
print(calculate_grade(marks))
    
