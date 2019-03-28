
# class myClass():
#   def method1(self):
#     print("Self can be use to manage the code")
#   def method2(self,passstring):
#     print("this is a string and the next string pass by user response"+" "+passstring)

# def main():
#   c = myClass()
#   c.method1()
#   c.method2("Dynamic String")

# if __name__ == "__main__":
#   main()  
# ------------------------ONE CLASS INHERIT OTHER CLASS-----------------------

#  important note i check it to try define function in class but show me this type of  error " Exception has occurred: TypeError
# method1() takes 0 positional arguments but 1 was given" so that
# you can use self keyword for fixing this problem

class myClass():
  
  def method1(self,stringCode):
    print("hello world"+" "+stringCode)
  
  def method2(self,cube):
    x  = cube * cube * cube
    print("the cube is of the number "+" "+str(cube)+" "+ "is :" +str(x))

class anotherClass():
  c = myClass()
  c.method1("Dynamic code")

  def name(self,name):
    print("kashif naqvi"+" "+name)
  c.method2(4)

def main():
  c = anotherClass()
  c.name("Hassan naqvi")

if __name__ == "__main__":
    main()

# ------------------------NEW EXAMPLE----------------------------------------

class name():

  def names(self):
    print("hello world")
  
  def code(self):
    print("code is art")


class code(name):

  def codeing(self,codeingBolts):
    name.names(self)
    name.code(self)
    print("i can use one class to another class define the code of the programming"+codeingBolts)


def main():
  c = code()
  c.codeing(" Dynamic code put in child class")

if __name__ == "__main__":
    main()