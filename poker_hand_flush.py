#Determine if the poker hand is flush, meaning if the five cards are of the same suit.

def is_flush(cards):
  h = []
  s = []
  d = []
  c = []
  for x in cards:
    if "S" in x:
      s.append(x)
    elif "H" in x:
      h.append(x)
    elif "D" in x:
      d.append(x)
    else:
      c.append(x)
  if len(s) == 5 or len(h) == 5 or len(d) == 5 or len(c) == 5:
    print(True)
  else:
    print(False)
    

is_flush(["AS", "3S", "9S", "KS", "4S"])#, True)
is_flush(["AD", "4S", "7H", "KC", "5S"])#, False)
is_flush(["AD", "4S", "10H", "KC", "5S"])#, False)
is_flush(["QD", "4D", "10D", "KD", "5D"])#, True)