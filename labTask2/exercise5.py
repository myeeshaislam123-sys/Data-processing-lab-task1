#Create a dictionary containing a student's name, ID, department, and CGPA. Print each key and value using a for loop. Then check the CGPA and display 'Good Standing' if the CGPA is 2.50 or higher; otherwise display 'Academic Warning'.
student={"stu name":"name","stu id":"id","dept":"dept","cgpa":3.4}
for i in student:
    print(i)
if student["cgpa"]>=2.50:
        print("Good Standing")
else:
        print("Academic Warning")
