#q1
for a in range(5):
    print("hello")

#q2
for a in range(10):
    print(a)

#q3
for i in range(11):
    print(i)

#q4
for i in range(10,0,-1):
    print(i)

#q5
for i in range(5,50,5):
    print(i)

#q6
for i in range(2,20):
    if i%2==0:
        print(i)

    #q7
for i in range(1,19):
    if i%2==1:
        print(i) 

#q8
for i in range(2,20):
 if i%3==0:
    print(i)
    
# Example:
for i in range(5,51,5):
    print(i)

#q9
for i in range(20,1,-1):
    print(i)

#q10
n=int(input("Enter your number :"))
for i in range(1,n+1):
    print(i)

# q11
n=int(input("Enter your number:"))
for i in range(1,n+1):
   if  i%2==0:
      print(i)

#q12
n=int(input("Enter your number:"))
for i in range(1,n+1):
   if  i%2==1:
      print(i)
       
#q13
n=int(input("Enter your number:"))
for i in range(1,n):
    if i%3==0:
        print(i)
    
#q14
n=int(input("Enter your number:"))
for i in range(1 ,n+1):
    if i%2==0 and i%3==0:
        print(f"{i} Divisible by both 2 and 3")
                  
#q15
n=int(input("Enter your number:"))
for i in range(0,n+1):
    if i%2==0:
        print(f"{i}:Even")

#q16
n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)

#q17
n = int(input("Enter a Number:-"))

for i in range(1, n + 1):
    if i%2==0:
     print(i) 

#q18
n = int(input("Enter a Number:-"))

for i in range(1, n + 1):
    if i%2==1:
     print(i) 

#q19
n = int(input("Enter a Number:-"))

for i in range(1,11):
      print(i*n)

#q20
n = int(input("Enter n: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Product:", fact)

# q21
name=str(input("Enter a Name:-"))
for i in name:
    print(i)

#q22
name=str(input("Enter a Name:-"))
for i in name:
    print(i,end="")

#q23
name=str(input("Enter a Name:-"))
count=0

for i in name:
    count=count+1
print("Charecter:-",count)

#q24
name=str(input("Enter a Name:-"))
count=0

for i in name:
  if i=="a":
    count=count+1
print("count",count)    
  
#q25
name=str(input("Enter a Name:-"))
count=0

for i in name:
    if "A"<=i<="Z":
        count=count+1
print("Upper charecter :",count)

#q26
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

#q27
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

#q28
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()

#q29
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()    

#q30
for i in range(1,6):
    for j in range(1,6):
        print(i*j,end=" ")
    print()    

#q31
n=int(input("Enter a Number:-"))
n=int(input("Enter a Number:-"))



for i in range(1,n+1,):
    for j in range(1,i+1):
        print(j,end="")
    print()  

for i in range(n+1,1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()    