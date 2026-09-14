#q1
num=int(input("Enter your number :"))

if num>=0:
    print("positive:")
elif num<=0:
    print("Negative:")
elif num==0:
    print("zero:")
else:
    print("Enter a valid number:")    
   
#q2
num=int(input("enter your number :"))
if num>0 and num%2==0:
    print("even positive")
elif num>0 and num%2!=0:
        print("odd positive")
elif num < 0 and num%2==0:
      print("even nagative")
elif num<0 and num%2!=0:
      print("odd nagative") 
else:
      print("(-_-):zero:(-_-)")           

#q3
num1=int(input("enter your first number :"))
num2=int(input("enter your second number :"))
if num1>num2:
    print(f"This condition corect{num1}:")
elif num2>num1:
    print(f"This condition corect{num2} ")    
else:
    print("Both are equal :")

#q4
num1=int(input("Enteer your first number :"))
num2=int(input("Enter your second number :"))
num3=int(input("Enter your thard number :"))
if num2>num1<num3:
    print(f"first number is small:{num1}")
elif num1>num2<num3 :
    print(f"second number is small:{num2}")   
else:
    print(f"theard number is small:{num3}")      

#q5
num1=int(input("Enteer your first number :"))
num2=int(input("Enter your second number :"))
num3=int(input("Enter your thard number :"))
if num2 < num1 > num3:
    print(f"first number is largest:{num1}")
elif num1 < num2 > num3 :
    print(f"second number is largest:{num2}")   
elif num1 < num3 >num2:
    print(f"theard number is largest:{num3}") 

#q6
num=int(input("Enter your number :"))
if num%5==0 and num%11==0:
    print("Divisible by both 5 and 11")
elif num%5==0:
    print("Divisible only by 5 :")
elif num%11==0:
    print("Divisible only by 11 :")
else:
    print("Divisible by neither :")

#q7
num=int(input("Enter your number :"))
if num/3 and num/7==0:
    print("Divisible by both 3 and 7")
elif num/3==0 or num/7!=0:
    print("Divisible only by 3")
elif num/7==0 or num/3==0:
    print("Divisible only by 7")
else:
    print("Divisible by Neither:")

#q8
marks=float(input("Enter your mnarks :"))
if marks==0 or marks==100:
    print("Invalid marks")
elif marks>=40:
    print("Pass") 
else:
    print("Fail") 

#q9
marks=float(input("Enter your marks:"))
if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<=89:
    print("B")
elif marks>=70 and marks<=79:
    print("C")
elif marks>=60 and marks<=69:
    print("D")
elif  marks>=40 and marks<=59:
    print("E")
elif marks<=40:
    print("Fail")
elif marks<=0 or marks>=100:
    print("invalid")
else:
    print("Invalied marks:") 

#q10
age=int(input("Enter your age :"))
if age<0:
    print("Invalid age")
elif age<18:
    print("Cannot vote")
elif age>=18 and age<120:
    print("Can vote")
else:
    print("Also are not vate")    

#q11
year=int(input("Enter a year :"))
if year%4==0 and  year%100!=0:
    print("Leap year")
elif year%400==0:
    print("leap year")
else:
    print("not a leap year")

## q12##############
exa=input("Enter you number [1 A @ a]:")
if exa.upper():
    print("Uppercase alphabet")
elif exa.lower():
    print("Lowercase alphabet")
elif exa.isdigit():
    print("Digit")
else:
    print("Invalid charecter")

#q13
text=input("Enter you charectar:")
if ("a"<=text>="z") or ("A"<=text>="Z"):
    if text.upper() == "U"or text.upper() == "E" or text.upper() == "O" or text.upper() == "I" or text.upper() == "A":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalied input")

#q14
cost_price=int(input("Enter cost_price price:-"))
selling_price=int(input("Enter selling_price price:-"))
if cost_price  < selling_price or cost_price  > selling_price:
   
   if cost_price  < selling_price:
      print("profit")
   
   elif cost_price > selling_price:
       print("lost")
else:
   print("No profiet no lost")   

#q15
a=int(input("Enter you cost price:"))
b=int(input("Enter you selling price:"))
if  b>a and b-a/a*100:
    print("profit_percentage")
elif b<a and a-b/b*100:
    print("lost_percentage")

#q16
units=int(input("Enter you unit:"))

if units<=100:
    print(f"total:{units*5}")

elif  units<=200:
    first_hundred=100*5
    rimaning_unit=(units-100)*7
    print(F"total:{first_hundred+rimaning_unit:}")
    
else:
    first_hundred=100*5
    next100_units=100*7
    rimaning_unit=(units-200)*10
    print(f"total:{first_hundred+next100_units+rimaning_unit}")
   

#q17
First_number=int(input("Enter you number:"))
Second_number=int(input("Enter you number:"))
a=input("Enter you oparator + - / *:")

if a=="+":
    print(f"result:{First_number+Second_number}")
elif a=="-":
    print(f"result{First_number-Second_number}")
elif a=="*":
    print(f"result:{First_number*Second_number}")
elif a=="/":
    print(f"result{First_number/Second_number}")
else:
    print("Enter you corect opareter")

#q18
a=int(input("Enter you Tmpareture:-"))

if a<0:
    print("Freezing")
elif 1 <= a <= 15:
    print("Very Cold")
elif 16 <= a <= 25:
    print("Cold")   
elif 26 <= a <= 35:
    print("Normal")
elif a>35:
    print("Hot") 

#q19
num=int(input("Enterr you Number:"))

if 0<= num <=10:
    print("Number is between 0-10:")
elif 11<= num <=50:
    print("Number is between 11-50:")
elif 51<= num <=100:
    print("Number is between 51-100:")

#q20
a=int(input("Enter you a value:"))
b=int(input("Enter you b value:"))
c=int(input("Enter you c value:"))

if a+b>c and a+c>b and b+c>a:
    print("valid triangle;")
else:
    print("Invalid triangle;")

#q21
a=int(input("Enter you a value:"))
b=int(input("Enter you b value:"))
c=int(input("Enter you c value:"))

if a+b>c and a+c>b and b+c>a:
    print("All three side different;")
elif a==b or b==c or c==a:
    print("Exactly two side equal;")
else:
    print("Exactly one side equal;")

#q22
a=float(input("Enter you Account balance:"))
b=float(input("Enter you withdrawal amount:"))

if b>0 and b%100 ==0 and b<=a and a-b>=500:
    remaining_balance=a-b
    print("Withdrawal successful")
    print(f"Remaining balance: {int(remaining_balance)}")
else:
    print("Withdrawal failed")

#q23
Username = input("Enter Username:-")
Password = input("Enter password:-")
if Username == "admin" and Password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")

#q24
purchase_amount=input("Enter you purchase amount:")

if purchase_amount<500:
    discount_pr = 0
elif purchase_amount<1000:
    discount_pr = 5
elif purchase_amount<2000:
    discount_pr = 10
elif purchase_amount<5000: 
    discount_pr = 15   
else:
    discount_pct = 20

discount_amount = (purchase_amount * discount_pct) / 100
final_amount = purchase_amount - discount_amount   

print(f"Original amount:{purchase_amount}")
print(f"Discount percentage:{discount_pr}")
print(f"Discount amount:{(purchase_amount * discount_pct) / 100}")
print(f"final_amount : {purchase_amount - discount_amount}")

#q25
sub1=float(input("Enter sub1 marks:"))
sub2=float(input("Enter sub2 marks:"))
sub3=float(input("Enter sub3 marks:"))

if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
    print("marks is 0to100:")
elif sub1<35 or sub2<35 or sub3<35:
    print("Result:Fail")  
else:
    Avareg=(sub1+sub2+sub3)/3
    print(f"Averag marks:{Avareg:.2f}")
    if Avareg>=75:
        print("Distinction")
    elif Avareg>=60:
        print("First class")  
    elif Avareg>=50:
        print("Second class")   
    elif Avareg>=35:
        print("pass")       
   
#q26     (^_^)

Day=int(input("Entyer Day:"))
Month=int(input("Entyer Month:"))
Year=int(input("Entyer year:"))

if  Month==2 or Day==29:
    Year%4==0 and Year%100!=0
    print(f"{Day}/{Month}/{Year}=>Valid")
else:
    print(f"{Day}/{Month}/{Year}=>Invalid")    
      
#q27
Hours=int(input("Enter Time in Hours:"))
Minutes=int(input("Enter Time in Minutes:"))
Seconds=int(input("Enter Time in Second:"))

if Hours<24 and Minutes<60 and Seconds<60:
    print(f"{Hours}:{Minutes}:{Seconds}=>valid")
else:
    print(f"{Hours}:{Minutes}:{Seconds}=>Invalid")

#q28
age1 = int(input("Enter Person1 age:"))
Name1 = input("Enter your Name:")
age2 = int(input("Enter Person2 age:"))
Name2 = input("Enter your Name:")
age3 = int(input("Enter Person3 age:"))
Name3 = input("Enter your Name:")

if age1 == age2 == age3:
    print("All three persons have the same age.")
elif age1 == age2 and age1 < age3:
    print(f"{Name1} and {Name2} are both the youngest.")
elif age1 == age3 and age1 < age2:
    print(f"{Name1} and {Name3} are both the youngest.")
elif age2 == age3 and age2 < age1:
    print(f"{Name2} and {Name3} are both the youngest.")
elif age1 < age2 and age1 < age3:
    print(f"{Name1} is youngest.")
elif age2 < age1 and age2 < age3:
    print(f"{Name2} is youngest.")
elif age3 < age1 and age3 < age2:
    print(f"{Name3} is youngest.")
else:
    print(f"{Name2} and {Name3} are both the youngest.")     


#q29
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Therd Number:"))

if b<a<c or c<a<b:
    print("Second largest number is {a}")
elif a<b<c or c<b<a:
    print("Second largest number is {b}")
else:
    print("Second largest number is {c}")

#q30
Student_age=int(input("Enter age:"))
Marks=int(input("Enter Marks:"))
Family_income=int(input("Enter Family income:"))
Attendance_percentage=int(input("Enter Attendance percentage:"))

if 18<Student_age<25 and Marks>=85 and Attendance_percentage>75 and Family_income<300000:
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")
    if Student_age>25:
        print("Student_age is not comapalited::")
    elif Marks<85:
        print("Marks is not compalited:")
    elif Attendance_percentage<75:
        print("Attendance_percentage not compalited:")
    else:
        print("Family income is not compalited:")