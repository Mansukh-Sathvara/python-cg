#q1
for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()    

#q2
for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()    

#extra
# n=int(input("Enter rows Number:"))
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

#q3
for i in range(1,4):
    for j in range(1,4):
        print(i,end=" ")
    print()    

#q4
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
    
#q5
for i in range(6,1,-1):
    for j in range(0,i-1):
        print("* ",end=" ")
    print()    

#q6
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

#q7
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()    

#q8
for i in range(1,6):
    for j in range(1,11):
        print(i*j, end=" ")
    print() 

n=int(input("Enter tabel number:"))     # # input type

for i in range(1,n+1):
    for j in range(1,11):
        print(i*j,end=" ")
    print()    

#q9
for i in range(1,4):
    for j in range(1,6):
        print(i*j, end=" ")
    print()    

#q10
for i in range(1,6):
    for j in range(1,6):
        print(j*j, end=" ")
    print()

#q11
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(j), end=" ")
    print()    

n=int(input("Enter Number:"))

for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j),end=" ")     
    print()

#q12
for i in range(1,6):
    for j in range(65,65+i):
        print(chr(64+i),end=" ")
    print()    

n=int(input("Enter number:"))

for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(64+i),end=" ")
    print() 

#q13
for i in range(1,6):
    for j in range(1,i+1):
        print(j*2-1,end=" ")
    print()    

#q14
for i in range(1,6):
    for j in range(1,i+1):
        print(j*2,end=" ")
    print()

# q15
for i in range(5):
    for j in range(5):
        print("*",end=" ") 
    print()    

#q16
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ") 
    print() 

#q17













#q21
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()    

#q22
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()    
#Q23
for i in range(6):
    for j in range(1,6-i):
        print(j,end=" ")
    print()    

#q24
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()    

n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()    

#q25
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()    
