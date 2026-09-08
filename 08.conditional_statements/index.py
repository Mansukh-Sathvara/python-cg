a=int(input("Enter your Number :"))

if a>10:
    print("your number is corect :")

q2
a=int(input("Enter your age :"))

if a>18:
    print("Your are a Adult")

q3
num=float(input("Enter your number :"))
if num>0:
    print("Positive")

q4
marks=float(input("Enter your marks :"))
if marks>=40:
    print("your are pass.")

q5
a=int(input("Enter your your number :"))

if a==0:
    print("zero")

q6
num=int(input("enter your number :"))
if num>0:
    print("positive :")

else:
    print("Not positive :")       

q7
age=int(input("Enter your age :"))
if age>=18:
    print("Your are Adult :")

else:
    print("your are Minor :")    

q8
num=int(input("enter your number :"))
if num%2==0:
    print("even number :")

else:
    print("odd number :")

q9
marks=float(input("Enter your marks :"))
if marks>=40:
    print("Your are a pass :")

else:
    print("Your are a fail :")    

q10
num1=float(input("enter your first number :"))
num2=float(input("enter your second number :"))
if num1>=num2:
    print("First number is greater :")
else :
  
    print("Second number is not greater :")

#q11
marks=float(input("Enter your number :"))
if marks>=90:
    print("Graed :A")
elif marks>=80:
    print("Graed :B")
elif marks>=70:
    print("Graed :C")    
elif marks>=60:
    print("Graed :D")
elif marks>=50:    
    print("Graed :F")
      
#  q12
num=float(input("Enter youur number :"))

if num==0:
    print("Number:-Zero")
elif num>=0:
    print("Number:-positive")
else:
    print("Number:-Negative")

#q13
day=int(input("Enter your number :1 2 3 4 5:"))

if day==1:
    print("Monday") 
elif day==2:
    print("Tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("Thursday")    
else:
    print("Friday")

#q14
marks=int(input("Enter your marks :"))
if marks>=90:
    print("Excellent")
elif marks>=80:
    print("Good")    
elif marks>=33:
    print("Pass")
elif marks<=33:
    print("Fail")    

#q15
age=int(input("Enter your age :-"))
if age<=18:
    print("Your are minor.")
else:
    print("Your are adult.")

#q16
a=int(input("Enter your number :1 2 3 "))
if a==1:
    print("Number is 1")
elif a==2:
    print("Number is 2")
elif a==3 :
    print("Number is 3")
else:
    print("others")    

#q17
marks=int(input("Enter your marks :"))
if marks>=90:
    print("Good")    
elif marks>=80:
    print("Pass")
else: 
    print("Failed")

#q18
num=int(input("Enter your number :"))
if num>=100:
    print("positive")
elif num<=100:
    print("Negative")    
else:
    print("zero")    

#q19
age=int(input("Enter your age :"))
if age>=18:
    print("adult")
elif age>=60:
    print("old")
else:
    print("minor")

q20
num=int(input("Enter your number :"))
if num%10!=0:
    if num>0:
        print("number is non-zero as well as positive!")
    else:
        print("number is non-zero as well as negative!")
else:
    print("number has zero!")

#q21
marks=int(input("Enter your marks :"))
age=int(input("Enter your age :"))
if age>=18 and marks>=40:
    print("Eligible")
else:
    print("Not eligibel")

#q22
number=int(input("Enter your number :"))
if number<10 or number>100:
    print("Special")
else:
    print("Not special")

#q23
age=int(input("Enter your age :"))
has_id=bool(input("Enter your id :"))
if age >= 18 and has_id== True:
    print("Allowed.")
else:
    print("Not Allowed.")

#q24
a=int(input("Enter your first number :"))   
b=int(input("Enter your second number :"))
if a>10 and b>10 :
    print("Both are greater than 10")
else:
    print("Not Both are greater than 10")    

#q25
a=int(input("Enter your number :"))
b=int(input("Enter your number :"))
if a<0 or b>100:
    print("This condition is true:")
else:
    print("This condition is false:")    

#q26
is_closed=False
if not is_closed:
    print("open")

# #q27
a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
if a>=10 and b<=50:
    print("This answer is corect :")
else:
    print("This answer is not corect :")

#28
a=int(input("Enter your first number :"))
b=int(input("Enter your second number :"))
if a>=10 or b<=50:
    print("number is outside :")
else:
    print("number is in range :")

#q29
is_student=bool(input("Enter your number :").capitalize())
has_id=bool(input("Enter your number :").capitalize())
has_ticket=bool(input("Enter your number :").capitalize())
if is_student==True and has_id==True and has_ticket==True:
    print("Allowed")
else:
    print("not Allowed")    

q30
age=int(input("enter age:"))
marks=int(input("enter marks:"))
has_id=int(input("enter id:"))
if age >= 18 and marks >= 40 and has_id==True :
    print("eligible")
else:
    print("not eligible")