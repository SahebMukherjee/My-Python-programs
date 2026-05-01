name = input("Enter student name:")
roll = input("Enter roll number:")
sub1 = float(input("Enter marks of subject1:"))
sub2 = float(input("Enter marks of subject2:"))
sub3 = float(input("Enter marks of subject3:"))
total = sub1 + sub2 + sub3
percentage = total/3
print("Name:",name)
print("Roll No:",roll)
print("Total Marks:",total)
print("Percentage:",percentage)
if percentage >= 40:
    print("Result:PASS")
else:
    print("Result:FAIL")
