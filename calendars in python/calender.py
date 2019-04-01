import calendar

# plain text calendar
c  = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2019,3,0,0)
print(st)

                  # Output:
                              # Su Mo Tu We Th Fr Sa
                              #                 1  2
                              #  3  4  5  6  7  8  9
                              # 10 11 12 13 14 15 16
                              # 17 18 19 20 21 22 23
                              # 24 25 26 27 28 29 30
                              # 31
# html calendar

hc = calendar.HTMLCalendar(calendar.SUNDAY)
ht = hc.formatmonth(2019,3)
print(ht)

# output:
        # <table border="0" cellpadding="0" cellspacing="0" class="month">
        # <tr><th colspan="7" class="month">March 2019</th></tr>
        # <tr><th class="sun">Sun</th><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th></tr>
        # <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="fri">1</td><td class="sat">2</td></tr>
        # <tr><td class="sun">3</td><td class="mon">4</td><td class="tue">5</td><td class="wed">6</td><td class="thu">7</td><td class="fri">8</td><td class="sat">9</td></tr>
        # <tr><td class="sun">10</td><td class="mon">11</td><td class="tue">12</td><td class="wed">13</td><td class="thu">14</td><td class="fri">15</td><td class="sat">16</td></tr>
        # <tr><td class="sun">17</td><td class="mon">18</td><td class="tue">19</td><td class="wed">20</td><td class="thu">21</td><td class="fri">22</td><td class="sat">23</td></tr>
        # <tr><td class="sun">24</td><td class="mon">25</td><td class="tue">26</td><td class="wed">27</td><td class="thu">28</td><td class="fri">29</td><td class="sat">30</td></tr>
        # <tr><td class="sun">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
        # </table>

for name in calendar.month_name:
  print(name)

# output:
#         January
#         February
#         March
#         April
#         May
#         June
#         July
#         August
#         September
#         October
#         November
#         December

for day in calendar.day_name:
  print(day)

# output:
#       Monday
#       Tuesday
#       Wednesday
#       Thursday
#       Friday
#       Saturday
#       Sunday


# for example peoples of office meeting on first  friday of every month 
print("team meeting is:")
for m in range(1,13):
  cal = calendar.monthcalendar(2019,m)
  weekone = cal[0]
  weektwo = cal[1]
  if weekone[calendar.FRIDAY] !=0:
    meetday = weekone[calendar.FRIDAY]
  else:
    meetday = weektwo[calendar.FRIDAY]
  print("%10s %2d "%(calendar.month_name[m],meetday))
  # output:
  #   team meeting is:
                            #   January  5
                            #   February  2
                            #     March  2
                            #     April  6
                            #       May  4
                            #       June  1
                            #       July  6
                            #     August  3
                            # September  7
                            #   October  5
                            #   November  2
                            #   December  7
                            # ----------------