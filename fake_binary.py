"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string."""

def fake_bin(x):
  y = str(x)
  new = []
  for i in y:
    if int(i) < 5:
      new.append('0')
    else:
      new.append('1')
  print(''.join(new))


fake_bin(3455489347545) #0011011001101