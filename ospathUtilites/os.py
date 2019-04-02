import os 
from os import path
import datetime
from datetime import time,timedelta,date

def main():
  print(os.name)
# output:posix
  print("Items exists",str(path.exists("code.txt")))
  print("Itme is file",str(path.isfile("code.txt")))
  print("item is directory",str(path.isdir("code.txt")))
  # output:
  #   Items exists True
  #   Itme is file True
  #   item is directory False

  print("Item path:" +str(path.realpath("code.py")) )
  print("item path and name:"+str(path.split(path.realpath("code.py"))))
  # output:
  #     Item path:/home/kashif/my_Data/Python/Learning Python/learning/code.py
  #     item path and name:('/home/kashif/my_Data/Python/Learning Python/learning', 'code.py')
  
  #get the modification time 
  print(datetime.datetime.fromtimestamp(path.getmtime("code.txt")))
  # output: 2019-04-01 19:23:21.259003

if __name__ == "__main__":
    main()





