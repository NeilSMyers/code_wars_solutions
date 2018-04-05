"""Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number."""

def Descending_Order(num):
  print(int(''.join(sorted(str(num),reverse=True))))
 

Descending_Order(0)#, 0)
Descending_Order(15)#, 51)
Descending_Order(123456789)#, 987654321)