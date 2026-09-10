# #q1
# num=int(input("Enter your number :"))

# if num>=0:
#     print("positive:")
# elif num<=0:
#     print("Negative:")
# elif num==0:
#     print("zero:")
# else:
#     print("Enter a valid number:")    
   
# #q2
# num=int(input("enter your number :"))
# if num>0 and num%2==0:
#     print("even positive")
# elif num>0 and num%2!=0:
#         print("odd positive")
# elif num < 0 and num%2==0:
#       print("even nagative")
# elif num<0 and num%2!=0:
#       print("odd nagative") 
# else:
#       print("(-_-):zero:(-_-)")           

# #q3
# num1=int(input("enter your first number :"))
# num2=int(input("enter your second number :"))
# if num1>num2:
#     print(f"This condition corect{num1}:")
# elif num2>num1:
#     print(f"This condition corect{num2} ")    
# else:
#     print("Both are equal :")

# #q4
# num1=int(input("Enteer your first number :"))
# num2=int(input("Enter your second number :"))
# num3=int(input("Enter your thard number :"))
# if num2>num1<num3:
#     print(f"first number is small:{num1}")
# elif num1>num2<num3 :
#     print(f"second number is small:{num2}")   
# else:
#     print(f"theard number is small:{num3}")      

# #q5
# num1=int(input("Enteer your first number :"))
# num2=int(input("Enter your second number :"))
# num3=int(input("Enter your thard number :"))
# if num2 < num1 > num3:
#     print(f"first number is largest:{num1}")
# elif num1 < num2 > num3 :
#     print(f"second number is largest:{num2}")   
# elif num1 < num3 >num2:
#     print(f"theard number is largest:{num3}") 

# #q6
# num=int(input("Enter your number :"))
# if num%5==0 and num%11==0:
#     print("Divisible by both 5 and 11")
# elif num%5==0:
#     print("Divisible only by 5 :")
# elif num%11==0:
#     print("Divisible only by 11 :")
# else:
#     print("Divisible by neither :")

# #q7
# num=int(input("Enter your number :"))
# if num/3 and num/7==0:
#     print("Divisible by both 3 and 7")
# elif num/3==0 or num/7!=0:
#     print("Divisible only by 3")
# elif num/7==0 or num/3==0:
#     print("Divisible only by 7")
# else:
#     print("Divisible by Neither:")

# #q8
# marks=float(input("Enter your mnarks :"))
# if marks==0 or marks==100:
#     print("Invalid marks")
# elif marks>=40:
#     print("Pass") 
# else:
#     print("Fail") 

# #q9
# marks=float(input("Enter your marks:"))
# if marks>=90 and marks<=100:
#     print("A")
# elif marks>=80 and marks<=89:
#     print("B")
# elif marks>=70 and marks<=79:
#     print("C")
# elif marks>=60 and marks<=69:
#     print("D")
# elif  marks>=40 and marks<=59:
#     print("E")
# elif marks<=40:
#     print("Fail")
# elif marks<=0 or marks>=100:
#     print("invalid")
# else:
#     print("Invalied marks:") 

# #q10
# age=int(input("Enter your age :"))
# if age<0:
#     print("Invalid age")
# elif age<18:
#     print("Cannot vote")
# elif age>=18 and age<120:
#     print("Can vote")
# else:
#     print("Also are not vate")    

# #q11
# year=int(input("Enter a year :"))
# if year%4==0 and  year%100!=0:
#     print("Leap year")
# elif year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")

### q12##############
# exa=input("Enter you number [1 A @ a]:")
# if exa.upper():
#     print("Uppercase alphabet")
# elif exa.lower():
#     print("Lowercase alphabet")
# elif exa.isdigit():
#     print("Digit")
# else:
#     print("Invalid charecter")

# #q13
# text=input("Enter you charectar:")
# if ("a"<=text>="z") or ("A"<=text>="Z"):
#     if text.upper() == "U"or text.upper() == "E" or text.upper() == "O" or text.upper() == "I" or text.upper() == "A":
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalied input")

# #q14
# cost_price=int(input("Enter cost_price price:-"))
# selling_price=int(input("Enter selling_price price:-"))
# if cost_price  < selling_price or cost_price  > selling_price:
   
#    if cost_price  < selling_price:
#       print("profit")
   
#    elif cost_price > selling_price:
#        print("lost")
# else:
#    print("No profiet no lost")   

#q15
a=int(input("Enter you cost price:"))
b=int(input("Enter you selling price:"))
profit=b-a
lost=a-b
if profit/a*100:
    print("")