# When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.
# Now, let's assign another variable y to the variable x.
#This statement creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.


#type1
# a=5
# b=5.0
# c=2+6j
# print(type(a))
# print(type(b))     
# print(type(c))


#type2
# a= 'welcome to geeks for geeks'
# print(type(a))
# print(a[1])
# print(a[0:4])
# print(a[-5])

#type3 List are mutable, ordered sequence of elements. They are defined using square brackets [] and can contain elements of different data types.
# a= [1,2,3,4,5]
# print(type(a))    
# b = ["Geeks", "For", "Geeks", 4, 5]
# print(b)
# print(type(b))


#Tuple immutable, ordered sequence of elements. They are defined using parentheses () and can contain elements of different data types.
# initiate empty tuple
# tup1 = ()

# tup2 = ('Geeks', 'For')
# print("\nTuple with the use of String: ", tup2,tup1)

# tup1 = (1, 2, 3, 4, 5)

# access tuple items
# print(tup1[0])
# print(tup1[-1])
# print(tup1[-3])

#Type4 Truthy and Falsy Values
# if 1:
#     print("1 is truthy")

# if not 0:
#     print("0 is falsy")

#type5- 4. Set Data Type
#unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined

s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

