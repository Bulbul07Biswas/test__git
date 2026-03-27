
# def div(x):
#     if x%2==0:
#         print(x,f":is even")
#     else:
#         print(x,f":number is odd")
# div(45)
# div(28)
# div(44.4) #yaha 44.4 k liye op odd hoga, bcz div k bad 0.4 ayega and even/odd Int i.e. 2,5,pr work karta hai.


# def evenOdd(x):
#     if x%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(evenOdd(48))
# print(evenOdd(77))

#Type1-1. Default Arguments
# def myfun(x,y=25):
#     return x,y
# print(myfun(10))
# print(myfun(12))

#Type-2 Keyword Arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.

# def student(sName,sSub):
#     return sName,sSub
# print(student(sName='Rani',sSub='History'))
# print(student(sSub='Physics',sName='Vikas'))


# Type3 Positional Arguments In positional arguments, values are assigned to parameters based on their order in the function call.

# def nameAge(name,age):
#     print('Hi my name is ',name)
#     print('My age is ',age)

# print('Case-1:')
# nameAge('Veena',25)

# print('\n Case-2:')
# nameAge(23,'Rohan')

#Type4- Arbitrary Arguments-n Python, arbitrary arguments allow a function to accept a variable number of inputs. This is done using two special symbols:
# *args: collects extra positional (non-keyword) arguments as a tuple.
# **kwargs: collects extra keyword arguments as a dictionary.

# def myFun(*args,**kwrags):
#     print("Non keyword argument (*args) is")
#     for arg in args:
#         print(arg)
#     print("\n Keyword arguments (**Krags) is")
#     for key,value in kwrags.items():
#         print(f"{key} - {value}")
# myFun('Indore','Food','Fashion',Capital='Delhi',Hobby='Dancing', Mall='Phonex')


# Type5-Function within Functions

# def f1():
#     a='Titanic'
#     def f2():
#         print(a)
#     f2()
# f1()
#Yaha phle f1 call hoga wo f1 mai jayega usse a milega fir wo def f2() mai jayega, yaha fun define hua hai abhi call nahi hua hai wo print abhi execute nahi hoga, an isse f2() mila ab wo fir f2() mai jayega and ab print krega
#---------------------------------------------------------------------------------

#Type 6- Anonymous Functions-a function is without a name, lambda keyword is used to create anonymous functions.
# def f1(x): return x*x*x
# f2= lambda x: x+2
# print(f1(2))
# print(f2(14))

#Type 7 Pass by Reference and Pass by Value
# Mutable objects: Changes inside the function affect the original object.- ex. list,dic
# Immutable objects: The original value remains unchanged.-Str,int

def f1(x):
    x[0]=10
lst=[5,15,29,40]
f1(lst)
print(lst)
#yaha mutable obj ki value change ho gai hai i.e. lst
def f2(x):
    x=20
a=10
f2(a)
print(a)
#yaha a ki value chnage nh hui bcx ye immutable hai


#Type 8 -Recursive Functions


def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

