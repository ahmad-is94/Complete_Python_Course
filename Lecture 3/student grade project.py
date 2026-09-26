name = input("Enter your name: ")
math = float(input("enter your marks : "))
english = float(input("enter your marks : "))
physics = float(input("enter your marks : "))
biology=float(input("enter your marks : "))
chemistry= float(input("enter your marks : "))

total = math + english + physics + biology + chemistry
percentage = total / 500 * 100
print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
  #if else statement 
if percentage>= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)
#PASS FAIL SYSTEM
if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")