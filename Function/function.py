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
