from datetime import datetime


def main():
  now = datetime.now()
  
  # %a represent the day name of week
  # %d represent the date
  # %B represent the month name
  # %Y represnet the Year 
  # print("current year is:",now.strftime("%a, %d,%B,%Y"))
  # OUTPUT:current year is: Thu, 28,March,2019
  # %B represent the full name of month but %b represent the small name like mar
  # print(now.strftime("%a"))
  # print(now.strftime("%b"))
  # print(now.strftime("only use this command you can find every thing:%c"))
  # # OUTPUT:Thu Mar 28 21:25:22 2019
  # print(now.strftime("THE TIME IS :%r"))
  # # THE TIME IS :09:38:37 PM
  # print(now.strftime("Define date :%x"))
  # # Define date :03/28/19
  # print(now.strftime("DEFINE DATE :%F"))
  # # DEFINE DATE :2019-03-28
  # print(now.strftime("DEFINE YEAR :%G"))
  # # DEFINE YEAR :2019
  # print(now.strftime("DEFINE 24 Hours:%X"))
  # DEFINE YEARS:21:38:37

  print(now.strftime("%c"))
  print(now.strftime("Current time is: %I:%M:%S:%p"))  
  # I represent to Hours M represent to minitus S represent to seconds p represent to morning/evening
if __name__ == "__main__":
    main() 
