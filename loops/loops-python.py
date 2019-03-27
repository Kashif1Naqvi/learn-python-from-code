# for loop

for i in range(5,9):
  print(i)

# output: 5,6,7,8

# while loop

i = 6
while i < 10:
   i = i + 1
   print(i)

# output: 7,8,9,10

# while loop with break statement

i = 2
while i < 10:
    if(i==5): break
    i = i +1
    print(i)

  # output:3,4,5


# for loop with continue statement

days = ["monday","tuesday","wednesday","thursday","friday","Satuarday","sunday"]

for i in days:
  print(i)

# output:
#         monday
#         tuesday
#         wednesday
#         thursday
#         friday
#         Satuarday
#         sunday

for i in range(1,20):
  if(i%2==0): continue
print(i)

# output:
    # 2
    # 4
    # 6
    # 8
    # 10
    # 12
    # 14
    # 16
    # 18

days = ["monday","tuesday","wednesday","thursday","friday","Satuarday","sunday"]

for i,d in  enumerate(days):
  print(i, d)

# output:
      # 0 monday
      # 1 tuesday
      # 2 wednesday
      # 3 thursday
      # 4 friday
      # 5 Satuarday
      # 6 sunday