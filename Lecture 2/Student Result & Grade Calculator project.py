name = input("enter  student name : ")
roll_number = input("enter roll number :")
#subjects markes
english = int(input("enter english marks : "))
math = int(input("enter math marks : "))
physics = int(input("enter physics marks : "))
computer = int(input("enter computer marks : "))
# Calculate Total\
total = english+math+physics+computer
#calculate percentage
percentage =  (total / 400) * 100
#calculate grading
if percentage >= 80:
    grade = "A"
elif percentage >=70:
    grade = "B"
elif  percentage >=60:
    grade = "C"
elif  percentage >=50:
    grade = "D"
else:
    grade = "F"
    print("Grade:", grade)

    # Pass / Fail
passed = percentage >= 50

if passed:
    status = "PASS"
else:
    status = "FAIL"

# Format Name
name = name.strip().title()

# Display Result
print("-----------------------------")
print("        STUDENT RESULT")
print("------------------------------")

print("Student Name :", name)
print("Roll Number  :", roll_number)

print("\nEnglish      :", english)
print("Math         :", math)
print("Physics      :", physics)
print("Computer     :", computer)

print("\nTotal Marks  :", total, "/ 400")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("Status       :", status)

print("-----------")