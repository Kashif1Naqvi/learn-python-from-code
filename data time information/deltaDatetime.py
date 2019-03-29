from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# today = datetime.now()

# print("Today date and time  is:",today)

# # output:Display the:Today date and time  is: 2019-03-29 14:20:37.251616


# print(timedelta(days=365,hours=2, minutes=33))

# # output:Displays the:365 days, 2:33:00

# print("After 1 year and 3 weeks later date and time is:",(str(today + timedelta(days=365,weeks=3))))

# # output will be:After 1 year and 3 weeks later date and time is: 2020-04-18 14:31:24.059720

# print("Date and time of 3 days and 2 weeks ago will be:",str(today - timedelta(days=3,weeks=3) ))

# # output will be:Date and time of 3 days and 3 weeks will be: 2019-03-05 14:42:53.505785


# # calculate the date 1 week ago ,formated as a string

# t = today  +  timedelta(weeks=1)
# print("the date is one week ago:",t.strftime("%A %B,%d %Y") )

# # output:the date and time is one week ago: Friday April,05 2019

# Muharam Days check........ 

today = date.today()
muharam=date(today.year,9,1)

if muharam < today:
  print("Muhram is already went by %d  ago " %((today-muharam).days))
  muharam = muharam.replace(year=today.year+1)

time_for_muharam = muharam-today 

print("it's just",time_for_muharam.days,"days untile for muharam")

# output:it's just 156 days untile for muharam


#  my Birthday program

today = date.today()

date_of_birth = date(today.year,8,14)

if today < date_of_birth:
  print("Syed Wajjhat date of birth went gone %d ago"%((date_of_birth-today).days))

time_for_syed_birthday = date_of_birth - today
print("it's just",time_for_syed_birthday.days,"days remaining syed wajjhat birthday")