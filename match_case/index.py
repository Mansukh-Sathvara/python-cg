#q1
choise=5
match choise:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")    
    case _:
        print("You selected Sandwich")    

#q2
settings=6

match settings:
    case 1:
        print("WI-FI")
    case 2:
        print(BLUETOOTH)  
    case 3:
        print("Mobaile Dataa")
    case 4:
        print("Airplane Mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Settings")            

#q3
choice=6

match choice:
    case 1:
        print("Chech Balance")
    case 2:
        print("Withdraw Money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change Pin")
    case 5:
        print("Exit")
    case _:
        print("INvalid Choice")                    

#q4
color="blue"

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Color")        

#q5
choice=6

match choice:
    case 1:
        print("view profile")
    case 2:
        print("view courses")
    case 3:
        print("view marks")
    case 4:
        print("view attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid Choice")            


#q6
choice=6

match choice:
    case 1:
        print("electronccs")
    case 2:
        print("Cloting")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print(exit) 
    case _:
        print("Invalid Choice")                   

#q7
choice=6

match choice:

    case 1:
        print("Account Balance")
    case 2:
        print(" Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("Invalid Choice")

#q8
choice=5
match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show") 
    case _:
        print("Invalid Choice")

#q9
n = input(
    "Enter Weather\n"
    "sunny\n"
    "rainy\n"
    "Cloudy\n"
    "Snowy\n"
    "Choice: "
).lower()

match n:
    case "Sunny":
        print("Wear sunglasses")
    case "Rainy":
        print("Take an umbrella")
    case "Cloudy":
        print("Carry a light jacket")
    case "Snowy":
        print("Wear warm clothes")
    case _:
        print("Invalid choice")

#q10
store = input(
    "Enter payment method:\n"
        "1. UPI\n"
    "2. Card\n"
    "3. Cash\n"
    "4. Wallet\n"
    "5. Another\n"
    "Choice: "
).lower()

match store:
    case "upi":
        print("UPI selected")
    case "card":
        print("Card selected")
    case "cash":
        print("Cash selected")
    case "wallet":
        print("Wallet selected")
    case "another":
        print("Another payment method selected")
    case _:
        print("Invalid payment method")

#q11
file_type = input(
    "Enter file type:\n"
    "1. pdf\n"
    "2. jpg\n"
    "3. png\n"
    "4. mp3\n"
    "5. mp4\n"
    "6. another\n"
    "Choice: "
)

match file_type:
    case "1":
        print("PDF")
    case "2":
        print("JPG")
    case "3":
        print("PNG")
    case "4":
        print("MP3")
    case "5":
        print("MP4")
    case "6":
        print("Another file type selected")
    case _:
        print("Invalid file type")

#q12
roles = input(
    "Enter role:\n"
    "1. admin\n"
    "2. teacher\n"
    "3. student\n"
    "4. guest\n"
    "Choice: "
).lower()

match roles:
    case "admin":
        print("Full Access")
    case "teacher":
        print("Manage class")
    case "student":
        print("View course")
    case "guest":
        print("Limited Access")
    case _:
        print("Invalid role")

#q13
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

#q14
priority=input("Enter number:")

match priority:
    case 1 | 2:
        print("Normal Priority:")
    case 3 | 4:
        print("Urgent Priority:")
    case _:
        print("other")

#q15
levels=input("Enter leaveals number:")

match levels:
    case 1 | 2:
        print("Basic Membership")
    case 3 | 4:
        print("Premium Membership")
    case _:
        print("other")

#q16
account="student"
condition=2

match account:
    case "student":
        match condition:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case _:
                print("View Attendance")
       
    case "teacher":
        match condition:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("View Attendance")
    case _:
        print("other persone")

#q17

account_type = int(input("Enter account type: "))
operation = int(input("Enter operation: "))


match account_type:
    case 1:
        print("Savings Account")
        
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case 2:
        print("Current Account")
    
        match operation:
            case 1:
                print("Check Balance Selected")
            case 2:
                print("Deposit Selected")
            case 3:
                print("Withdraw Selected")
            case _:
                print("Invalid Operation")
    case _:
        print("Invalid Account Type")

#q18
category=int(input("enter category Number:"))
product=int(input("Enter product Number:"))

match category:
    case 1:
        print("Electronics")
        match product:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case _:
                print("Headphones")
    case 2:
        print("Clothing")
        match product:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case _:
                print("Shoes")
    case _:
        print("Invalid category")

#q19
type_of_food=int(input("Enter Food Number:"))
type_of_menu=int(input("Enter Menu Number:"))

match type_of_food:
    case 1:
        print("Vegetarian")
        match type_of_menu:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg Biryani")
            case _:
                print("Invalid Menu")              
    case 2:
        print("Non-Vegetarian")
        match type_of_menu:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")      
            case _:
                print("Invalid Menu")      
    case _:
        print("Invalid Food")

#q20
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Enter operator:")

match op:
    case "+":
        print(f"Result :{num1 + num2}")
    case "-":
        print(f"Result:{num1 - num2}")
    case "/":
        print(f"Result:{num1 / num2}")
    case "*":
        print(f"Result:{num1 * num2}")    
    case _:
        print(f"Inavalied operater:{op}")

#q21
n=int(input("Enter a choice:"))
temperature=int(input("Enter a temperacher:"))
fahrenheit=int(input("Enter a temparecher:"))
match n:
    case 1:
        print(f"Fahrenheit={temperature*9/5+32}")
    case _P:
        print(f"Celsius={fahrenheit-32*5/9}")
    
#q22
n=int(input("Enter a menu:"))
value=int(input("Enter a value:"))

match n:
    case 1:
        print(f"{value * 1000} Meters")
    case 2:
        print(f"{value / 1000} Kilometers")
    case 3:
        print(f"{value * 1000} grams")
    case 4:
        print(f"{value / 1000} Kilograms")
    case _:
        print("Invalid conversion:")

#q23
n=int(input("Enter a ATM program:"))
amount=int(input("Enter a amount:"))
match n:
    case 1:
        print("Savings Account")
        if amount>0:           
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case 2:
        print("")
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
    case _:
        print("Ivalid amount")

#q24
n=int(input("Choice a Menu:"))
age=int(input("Enter a age:"))

match n:
    case 1:
        if age > 18:
            print("You can start the exam")
        else:
            print("Invalid age")
    case 2:
        print("Viewing Result")
    case 3:
        print("Exit")
    case _:
        print("Invalid choice:")

#q25
n=int(input("Enter ticket choice:"))
age=int(input("Enter a age:"))

match n:
    case 1:
        if age<=5:
            print("Free Entry")
        else:
            print("Regular Ticket")
    case 2:
        if age<=5:
            print("Free Entry")
        else:
            print("Premium Ticket")
    case 3:
        if age<=5:
            print("Free Entry")
        else:
            print("VIP Ticket")     
    case _:
        print("Invalid Ticket")            

#q26
device = int(input("Enter device: "))

match device:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("Invalid Device")

#q27
dept = int(input("Enter department: "))

match dept:
    case 1:
        print("General Medicine")
    case 2:
        print("Cardiology")
    case 3:
        print("Orthopedics")
    case 4:
        print("Pediatrics")
    case 5:
        print("Emergency")
    case _:
        print("Invalid Department")

#q28
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")
    case 2:
        print("Cancel Ticket Selected")
    case 3:
        print("Check PNR Selected")
    case 4:
        print("Train Schedule Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

#q29
choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Search Book Selected")
    case 2:
        print("Issue Book Selected")
    case 3:
        print("Return Book Selected")
    case 4:
        print("View Issued Books Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")

#q30
status = input("Enter status: ").strip().lower()

match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your food is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid Status")

#q31
banking_type = int(input("Enter banking type: "))
option = int(input("Enter option: "))

match banking_type:
    case 1: 
        match option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")

    case 2:  
        match option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")

#q32
role = int(input("Enter role (1-Student, 2-Teacher, 3-Parent): "))
option = int(input("Enter option: "))

match role:
    case 1:  # Student
        match option:
            case 1:
                print("Student Marks Selected")
            case 2:
                print("Student Attendance Selected")
            case 3:
                print("Student Homework Selected")
            case _:
                print("Invalid Option")

    case 2:  # Teacher
        match option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Teacher Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")

    case 3:  # Parent
        match option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")

#q33
transport = int(input("Enter transport (1-Flight, 2-Train, 3-Bus): "))
option = int(input("Enter class/option: "))

match transport:
    case 1:  
        match option:
            case 1:
                print("Flight - Economy Selected")
            case 2:
                print("Flight - Business Selected")
            case _:
                print("Invalid Option")

    case 2:  
        match option:
            case 1:
                print("Train - Sleeper Selected")
            case 2:
                print("Train - AC Selected")
            case _:
                print("Invalid Option")

    case 3:  
        match option:
            case 1:
                print("Bus - Ordinary Selected")
            case 2:
                print("Bus - Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport Selection")

#q34
choice = int(input("Enter choice (1-Start, 2-Load, 3-Settings, 4-Exit): "))

match choice:
    case 1:
        print("Start Game")

    case 2:
        print("Load Game")

    case 3:  
        setting_option = int(input("Enter setting option (1-Sound, 2-Graphics, 3-Controls): "))
        match setting_option:
            case 1:
                print("Sound Settings Selected")
            case 2:
                print("Graphics Settings Selected")
            case 3:
                print("Controls Settings Selected")
            case _:
                print("Invalid Setting Option")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")

#q35
category = int(input("Enter category (1-Starters, 2-Main Course, 3-Desserts, 4-Drinks): "))
item = int(input("Enter item: "))

match category:
    case 1:
        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Starter Option")

    case 2: 
        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Main Course Option")

    case 3: 
        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Dessert Option")

    case 4: 
        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Drink Option")

    case _:
        print("Invalid Category")

#q36
payment_type = int(input("Enter payment type (1-UPI, 2-Card, 3-Wallet): "))
option = int(input("Enter option: "))

match payment_type:
    case 1:  
        match option:
            case 1:
                print("Scan QR Selected")
            case 2:
                print("Enter UPI ID Selected")
            case _:
                print("Invalid Option")

    case 2: 
        match option:
            case 1:
                print("Credit Card Selected")
            case 2:
                print("Debit Card Selected")
            case _:
                print("Invalid Option")

    case 3:  
        match option:
            case 1:
                print("Add Money Selected")
            case 2:
                print("Pay Using Wallet Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Payment Type")

#q37
category = int(input("Enter category (1-Programming, 2-Mathematics, 3-Communication): "))
course = int(input("Enter course option: "))

match category:
    case 1:  
        match course:
            case 1:
                print("Python Selected")
            case 2:
                print("Java Selected")
            case 3:
                print("C++ Selected")
            case _:
                print("Invalid Programming Option")

    case 2:  
        match course:
            case 1:
                print("Algebra Selected")
            case 2:
                print("Calculus Selected")
            case 3:
                print("Statistics Selected")
            case _:
                print("Invalid Mathematics Option")

    case 3:  
        match course:
            case 1:
                print("English Selected")
            case 2:
                print("Presentation Selected")
            case 3:
                print("Interview Skills Selected")
            case _:
                print("Invalid Communication Option")

    case _:
        print("Invalid Category")

#q38
main_choice = int(input("Select an option: "))

match main_choice:
    case 1:
        sub_choice = int(input("Select option: "))
        
        match sub_choice:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Engine Option")

    case 2:
        sub_choice = int(input("Select option: "))
        
        match sub_choice:
            case 1:
                print("Headlights Turned On")
            case 2:
                print("Indicators Turned On")
            case 3:
                print("Hazard Lights Turned On")
            case _:
                print("Invalid Lights Option")

    case 3:
        sub_choice = int(input("Select option: "))
        
        match sub_choice:
            case 1:
                print("Playing Music")
            case 2:
                print("Music Paused")
            case 3:
                print("Playing Next Track")
            case 4:
                print("Playing Previous Track")
            case _:
                print("Invalid Music Option")

    case 4:
        sub_choice = int(input("Select option: "))
        
        match sub_choice:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Navigation Option")

    case _:
        print("Invalid Main Option")

#q40
print("--- College Portal ---")
print("1 -> Student")
print("2 -> Teacher")
print("3 -> Administration")

role = int(input("Enter role: "))

match role:
    case 1:
        # print("\n--- Student Options ---")
        # print("1 -> Profile")
        # print("2 -> Marks")
        # print("3 -> Attendance")
        # print("4 -> Courses")
        
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")

    case 2:
        # print("\n--- Teacher Options ---")
        # print("1 -> Students")
        # print("2 -> Enter Marks")
        # print("3 -> Attendance")
        # print("4 -> Courses")
        
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")

    case 3:
        # print("\n--- Administration Options ---")
        # print("1 -> Fees")
        # print("2 -> Admissions")
        # print("3 -> Notices")
        # print("4 -> Departments")
        
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("Opening Administration Fees")
            case 2:
                print("Opening Administration Admissions")
            case 3:
                print("Opening Administration Notices")
            case 4:
                print("Opening Administration Departments")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")




















