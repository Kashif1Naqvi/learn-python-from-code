
def main():
  # write a file
  # f = open("textfile.txt","w+")
  
  # add data in existing file

  # f = open("textfile.txt","a")
  # for i in range(10):
  #   f.write("this is code for learning "+str(i)+ "\n\r")
  # f.close()


  # for reading a file

  f = open("code.txt","r")
  if f.mode == 'r':
    contents = f.read()
    print(contents)
  f.close()

if __name__ == "__main__":
    main()