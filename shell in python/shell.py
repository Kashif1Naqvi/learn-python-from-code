import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile
def main():
  if(path.exists("textfile.txt")):
    src = path.realpath("textfile.txt")
    # dst = src + ".bak"
    # shutil.copy(src,dst)
    # shutil.copystat(src,dst)
    #output: in this way create a file with the name of textfile.txt.bak

    # rename the file 
   
    # os.rename("textfile.txt","newfile.txt")
    
    # output: file in rename now file name is newfile.txt

    # zip file
    # with ZipFile("testzip.zip") as newzip:
    #   newzip.write("file.txt")
    #   newzip.write("code.txt")
    with ZipFile('spam.zip', 'w') as myzip:
      myzip.write('file.txt')


if __name__ == "__main__":
    main()