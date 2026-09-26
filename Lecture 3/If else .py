#elegibilty of vote casting
age = 18
if age >= 18:
    print("eligible for vote")
    #else statement 
else:
    print("not eligible")


#elegibility of voting user defined



    #password checking strength
password = input("enter your password : ")

if len (password) >= 8:
 if any(char.isdigit() for char in password):
    print("password is strong")
 else:
    print("password must have a numerical number ")

else:
 print("password must have atleast 8 numbers .")
if age < 18: 
    print("You are not eligible to vote")  
if age >= 18:
     print("You are eligible to vote.")  
if age >= 21: 
    print("You are allowed to consume alcohol in some countries.")  
if age >= 60: 
      print("You are eligible for senior citizen benefits.")  
if age >= 80: 
    print("You are a very senior citizen. Take extra care of your health.")  




    #marks checking
    marks = int(input("enter your marks : "))
    if marks < 40:

        if marks >= 75:
            print("you are passed with high numbers : ")
        else:
            print("you passed the exam : ")
    else:
        print("you are failed . ")
        #elif statement
    temp = int(input("enter temp of the day : "))
    if temp >=30:
        print("today temperatue is warm ")
    elif temp >=20:
        print("hot day ")
    elif  temp >=10:
        print("its a normal day . ")
    else:
        print("its too cold . ")

        #grading system
        marks = int(input("enter the marks : "))
        if marks >= 85:
            print("grade a")
        elif marks >= 75:
            print("B")
        elif marks >= 65:
            print("C")
        elif marks >= 55:
            print("D")
        else:
            print("you are fail .")
            

                