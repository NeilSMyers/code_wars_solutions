# You will be given an array (a) and a value (x). All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not.

def check(seq, elem):
  print(elem in seq)


check((66, 101), 66)
check((78, 117, 110, 99, 104, 117, 107, 115), 8)
check((101, 45, 75, 105, 99, 107), 107)
check((80, 117, 115, 104, 45, 85, 112, 115), 45)
check(('t', 'e', 's', 't'), 'e')
check(("what", "a", "great", "kata"), "kat")
check((66, "codewars", 11, "alex loves pushups"), "alex loves pushups")
check(("come", "on", 110, "2500", 10, '!', 7, 15), "Come")
check(("when's", "the", "next", "Katathon?", 9, 7), "Katathon?")
check((8, 7, 5, "bored", "of", "writing", "tests", 115), 45)
check(("anyone", "want", "to", "hire", "me?"), "me?")