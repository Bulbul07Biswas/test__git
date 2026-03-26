
#type
# age= 20
# if age>21:
#     print("You can drive")
# else:
#     print("You cannot drive")

#type2- Short hand if

# age= 20
# if age>19: print("You can drive")
# else: print("You cannot drive")

#type3-elif-It allows us to check multiple conditions

# age= 10
# if age<=12:
#     print("You are a child")
# elif age<=19:
#     print("You are an Teenager")
# elif age<=35:
#     print("You are a young adult")
# else:
#     print("You are an adult")

#practice
#Check number is positive, negative or zero

# num = 0
# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")


#Q2: Age validation

# age = 87
# if age<18:
#     print("You are not elligible to vote")
# elif age>60:
#     print("You are Senior citizen")
# else:
#     print("you are elligible to vote")

#2 numbers input lo → bada kaun hai print karo
# x= int(input("Enter your first number:"))
# y= int(input("Emter your seconf number:"))

# if x>y:
#     print(x, f"this is greater than",y)
# else:
#     print(y, f" is greater", x)

#3 Login validation
# correct_id= "admin"
# correct_pw= "1234"

# if correct_id=="admin":
#     if correct_pw=="1234":
#         print("Login successfull")
#     else:
#         print("Invalid Password! pls try again")  
# else:
#     print("Invalid Id! pls try with valid id")


#4 Number divisable check by 3 and 5

# num = int(input("Enter the number:"))


# if num%5==0 and num%3==0:
#     print(num, f"is divisabl with both ")
# elif num%3==0:
#     print(num, f"is divisable by 3")
# elif num%5==0:
#     print(num, f"is divisable by 5")
# else:
#     print(num, f" is not divisable by 3 or 5")


#5 🔹 Q8: Form validation ⭐

# input:name,age,Conditions:name empty → "Name required",age < 18 → "Underage",otherwise → "Form submitted"

# user_name= input("Enter your name:")
# user_age= int(input("Enter your age:"))

# if user_name!="":
#     print(f"user name is",user_name)
#     if user_age>18:
#        print("Form submitted successfully!")
#     else:
#       print(user_name, f" Is Underage")
# else: 
#    print("Name required!")



