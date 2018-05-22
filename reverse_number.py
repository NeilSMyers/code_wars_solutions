# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

def reverse_number(n):
  if str(n)[0] == "-":
    print (-int(str(n)[:0:-1]))
  else:
    print(int(str(n)[::-1]))


reverse_number(123)#, 321)
reverse_number(-123)#, -321)
reverse_number(1000)#, 1)
reverse_number(4321234)#, 4321234)
reverse_number(5)#, 5)
reverse_number(0)#, 0)
reverse_number(98989898)#, 89898989)
