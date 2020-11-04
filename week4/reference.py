# https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])

   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


def changeint(a):
    a = 10
    print(a)
    return

a = 15
changeint(a)
print(a)


def changetuple(t):
    t = ("a", "b", "c")
    return

t = ("x", "y")
changetuple(t)

print(t)
