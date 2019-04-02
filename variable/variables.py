# Declear a variable 

f = 0

# Two Diffrent data Type Cannot be Combine
# so we can use str for combine two variables

# print("The string combine with:"+ str(5))

# define function

def functionDefine():
  global f
  f="funtion can be calll two time"
  print(f)

  # if i delete the variable then use to del for f

  # Exception has occurred: NameError
  # name 'f' is not defined
  #   File "/home/kashif/my_Data/Python/Learning Python/learning/variables.py", line 23, in <module>
  #     print(f)
  #   File "/usr/lib/python3.6/runpy.py", line 85, in _run_code
  #     exec(code, run_globals)
  #   File "/usr/lib/python3.6/runpy.py", line 96, in _run_module_code
functionDefine()
# del f
# del can be delete the defination of  previous variable declaration
# print(f)
