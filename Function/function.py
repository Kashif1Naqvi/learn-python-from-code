def name():
  print("Hello world")

# first show me the function declaration
name()
# with print show me the same result
print(name())
# But when i write the name only then show me the address of the funtion
print(name)


# output:
# Hello world
# Hello world
# None
# <function name at 0x7f665c216950>


# ---------------------------NEW EXAMPLE---------------------------------

def squre(x):
  return x * x

print(squre(3))

# Output:9
#---------------------------NEW EXAMPLE-----------------------------------

def cube(x):
  return x*x*x

print(cube(4))

# Output:64

# --------------------------NEW EXAMPLE------------------------------------
def name(arg1,arg2):
  print(arg1,"  ",arg2)

print(name("kashif","Shahzad"))

# output: Kashif  Shahzad

#--------------------------NEW EXAMPLE-------------------------------------
def power(num,x):
  result = 1 
  for i in range(x):
    result = result * num
  return result

print (power(2,2))

# output:4

# ------------------------NEW EXAMPLE---------------------------------------

def multipleData(*arg):
  result = 0
  for x in arg:
    result = result + x
  return result
print(multipleData(2,2,7))

# output: 11

# -----------------------END EXAMPLES----------------------------------------

print("Kashif Naqvi By You learn a lot from this chapter i think :) ")