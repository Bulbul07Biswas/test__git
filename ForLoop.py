# type 1
# n=4

# for i in range(0,n):
#     print(i)

#type2

# li= ["Banana", "mango","Chickoo"]
# for i in li:
#  print(i)

# tup= ("C","java","Python",'java', 'python')
# for i in tup:
#  print(i)

# name= 'Naman'
# for i in name:
#  print(i)

# dic ={'name':'Bunny','Age':4,'School':'MM'}
# for d in dic:
#  print(d)

#  set1={10,23,12,23,10,30}
#  for s in set1:
#   print(s)

#Type3- Iterating by Index of Sequences
# li= ['iPhone','Samsung','Nothing','OnePlus']
# for index in range(len(li)):
#     print(li[index])

#type4 - Continue Statemnet
# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)

#Type 5- Break Statement
# for letter in 'geeksforgeeks':
#     if letter == 'f' or letter == 'o':
#         break

# print('Current Letter :', letter)

#Type 6- Pass Statement
# for letter in 'mypythonprogramme':
#     pass
# print('last letter:', letter)


#Practice ChatGpt
#1 print 1 to 10

# for i in range(1,11):
#     print(i)

# 🔹 Q2: Even numbers print karo (1–20)
# for i in range(1,21):
#     if i%2==0:
#         print(i,f"Is even number")
#     else:
#        pass

# 🔹 Q3: Sum of numbers: 1 se 10 ka sum nikalo

total=0

# for i in range(1,11):
#     total=total+i
# print(total)

#🔹 Q4: Table print karo👉 User se number lo ,uska table print karo (1–10)

# num = int(input("Enter the number:"))
# for i in range(1,11):
#     x= num*i
#     print(x,"\n")

#🔹 Q5: Count vowels in string ⭐
a= 'automation'
count=0
for i in a:
    if i in 'aeiou':
      count= count+1
    print("Vowel count:", count)

