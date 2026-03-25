# When x = 5 is executed, Python creates an object to represent the value 5 and makes x reference this object.
# Now, let's assign another variable y to the variable x.
#This statement creates y and references the same object as x, not x itself. This is called a Shared Reference, where multiple variables reference the same object.

y = x
import sys
print(sys.version)