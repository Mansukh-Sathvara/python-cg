q23
total = 0
for i in range(5):
    num = int(input("Enter a num: "))
    total += num
print(total)

#q24
count = 0

for i in range(10):
    num = int(input("Enter num: "))
    if num % 2 == 0:
        count += 1
print(count)

#q26
lar = None

for i in range(5):
    n = int(input("Enter num: "))
    if lar is None or n > lar:
        lar = n
print(lar)

#q28
for i in range(20):
    n = int(input("Enter Number: "))
    if n % 2 == 0:
        print("even")

#q29
n = int(input("Enter num: "))
for i in range(1, 11):
    table = n * i
    print(table)

#q30
num = 0
for i in range(5):
    n = int(input("Enter Number: "))
    num += n
average = num / 5
print(average)

#q1

count_uppercase = 0
count_lowercase = 0
count_digits = 0
count_spaces = 0
count_special = 0

n = input("Enter a string ")
for character in n
	if character.isupper()
		count_uppercase += 1
	elif character.islower()
		count_lowercase += 1
	elif character.isdigit()
		count_digits += 1
	elif character.isspace()
		count_spaces += 1
	else:
		count_special += 1
		      
print("Uppercase", count_uppercase)
print("Lowercase", count_lowercase)
print("Digits", count_digits)
print("Spaces", count_spaces)
print("Special characters", count_special)

if count_uppercase > count_lowercase and count_uppercase > count_digits and	count_uppercase > count_special and count_uppercase > count_spaces
	print("studentuppercase")
elif count_lowercase > count_uppercase and 	count_uppercase > count_digits and count_lowercase > count_spaces and count_lowercase >count_special
	print("studentlowercase")
elif count_spaces > count_uppercase and count_spaces > count_lowercase and count_spaces > count_spaces and count_spaces > count_digits
	print("studentcount_spaces")	
elif count_special > count_uppercase and  count_special > count_lowercase and  count_special > count_digits and count_special > count_spaces
	print("studentcount_special")
elif count_digits > count_uppercase and count_digits > count_lowercase and count_digits > count_special and count_digits > count_spaces
	print("studentcount_digits")
else:
	print("Tie")
    

#q2
excellent=0
good=0
passed=0
fail=0

for i in range(4):
    marks=int(input("Enter marks-"))

    if 75 <= marks <=100:
        excellent+=1
    elif 50 <= marks <= 74:
        good+=1
    elif 35 <= marks <= 49:
       passed+=1
    else:
        fail+=1

print(f"student{{excellent}} {excellent}")
print(f"student{{good}} {good}")
print(f"student{{pas}} {passed}")
print(f"student{{fail}} {fail}")

#Q3
vowel = 0
consonant = 0
digit = 0
special_charecter = 0

n = input("Enter sentens:-")
for i in n:
    if i.lower() in "aeiou":
        vowel += 2
    elif i.isalpha():
        consonant += 1
    elif i.isdigit():
        digit += 3
    else:
        special_charecter += 4


print(f"vowel:{vowel}")
print(f"consonant:{consonant}")
print(f"digit:{digit}")
print(f"special_charecter:{special_charecter}")

if vowel > consonant and vowel > digit and vowel > special_charecter:
    print(f"vowel highest number:{vowel}")
elif consonant > vowel and consonant > digit and consonant >special_charecter:
    print(f"consonant highest number:{consonant}")
elif digit > vowel and digit > consonant and digit > special_charecter:
    print(f"digit highest number:{digit}")
else:
    print(f"special_charecter highest number:{special_charecter}")


#q4
upper=0
lower=0
digit=0
special_character=0
count=0
for i in range(5):
    n=(input("Enter password:-"))
   

if len(n)>=8:
    count += 1
for ch in n:    
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special_character += 1

print(f"uppercase:{upper}")
print(f"lowercase:{lower}")
print(f"digit:{digit}")
print(f"special_character:{special_character}")  

count = upper + lower + digit + special_character

if count == 5:
    print("strong")
elif count >= 3:
    print("Medium")
else:
    print("Weak")    

#q5
n=input("Enter sentence:-")
word=n.split()

short=0
medium=0
long=0

for i in word:
    length=len(word)

if len(n) <= 3:
    print(f"short:{len(n)}")
elif 4<= len(n) <=6:
    print(f"Medium:{len(n)}")
else:
    print(f"Long:{len(n)}")

#q6
even=0
odd=0

for i in range(5):
    n=str(input("Enter Number:-"))
    num=int(n)
    
    if num !=0 and num%2==0:
        even += 1
    elif num%2==1:
        odd += 1

print(f"even:{even}")        
print(f"odd:{odd}")        

if even == odd:
    print(f"equal number:{even},{odd}")
elif even > odd:
    print(f"highest even number:{even}")
else:
    print(f"highest odd number:{odd}")    

#q7
n=str(input("Enter string:"))
count_vowel=0
count_consonnet=0
count_same=0
letar=n

for i in letar:
    length=len(letar)

    if i in "aeiou" or i in "AOUIE":
        count_vowel += 1
    elif i.isalpha():
        count_consonnet += 1
    else:
        count_same += 1

print(f"vowels:{count_vowel}")   
print(f"consonnet:{count_consonnet}")  
print(f":{count_same}")    

if (count_vowel==2) + (count_consonnet==2):
    print("Duplicate")
elif (3 <= count_vowel <=4) + (3<= count_consonnet <=4):
    print("Repeated")
else:
    print("HIGHLY REPEA")

# extra ///
for i in range(1,6):
    for j in range(1,6):
        if j==1 or j==5 or i==5 or i==1 or i==3 and j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
    print()               

#q8
count_budget = 0
count_regular = 0
count_premium = 0
count_luxury = 0

total = 0

for i in range(8):

    n = int(input("Enter price: "))

    total += n

    if n < 500:
        count_budget += 1
        print("Budget")

    elif n <= 1999:
        count_regular += 1
        print("Regular")

    elif n <= 4999:
        count_premium += 1
        print("Premium")

    else:
        count_luxury += 1
        print("Luxury")


average = total / 8

print("Total:", total)
print("Budget:", count_budget)
print("Regular:", count_regular)
print("Premium:", count_premium)
print("Luxury:", count_luxury)
print("Average:", average)
#q9

n=str(input("Enter:-"))
vowel=0
consonant=0
digit=0
special_charecter=0
even=0
odd=0

for i in n:
  if i.isdigit():
    digit += 1
    if int(i)%2==0:
      even +=1
    elif int(i)%2==1:
      odd += 1  
  elif i  in "eaiouAEIOU":
      vowel+=1     
  elif i.isalpha():
    consonant += 1
  else:
    special_charecter += 1
    

print(f"digit:even_number:-{even}") 
print(f"digit:odd_number:-{odd}")
print(f"consonant:{consonant}")
print(f"digit:{digit}")
print(f"vowel:{vowel}")
print(f"special_charecter:{special_charecter}")

#q10
 













