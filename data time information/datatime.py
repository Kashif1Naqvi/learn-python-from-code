from datetime import date
from datetime import time
from datetime import datetime

today =date.today()
print("Today date is:",today)

#output:) 2019-03-28


days =["Monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

print("Today day is:",days[today.weekday()])

# output:) Today day is: thursday

print("today month date and year is:" ,today.month, str(today.day) ,days[today.weekday()], str(today.year) )

# output:today month date and year is: 3 28 thursday 2019

time = datetime.now()

print("the current date and time is:",time)

# output:the current date and time is: 2019-03-28 20:45:53.294074