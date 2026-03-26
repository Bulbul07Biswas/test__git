# Option1
# name= input("Enter Your Name:")
# print("Hello", name, "Welcome!")

#Option2- Print Multiple variables

# name= input("Enter your name:")
# age= input("Enter your age:")
# hobby= input("Enter your hobby:")
# print(name, age, hobby)

#Option3- Take multiple Inputs

# x, y = input("Enter two numbers: ").split()
# print(x , y)

# x,y = int(input("Enter two numbers :"))- This is wrong int ip can take one value at time
# x= int(input("Enter first number:"))
# y= int(input("Enter second number:"))
# print(x,y,x+y)

#Option4- Taking diff type of ip

# x= int(input("Enter your age:"))
# y= float(input("Evaluation result 7/2:"))
# print(x,y)


#Option5-Find DataType of Input in Python

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Take input from stdin in Python- means taking Ip from user just we did b4>> input(), "standard Ip"

# There are a number of ways in which we can take input from stdin in Python.
# sys.stdin
# input()
# fileinput.input()