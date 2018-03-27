# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

def replace_exclamation(s):
  print(s.replace('a', '!').replace('e','!').replace('i','!').replace('o','!').replace('u','!').replace('A','!').replace('E','!').replace('I','!').replace('O','!').replace('U','!'))
    

replace_exclamation("Hi!")
replace_exclamation("!Hi! Hi!")
replace_exclamation("aeiou")
replace_exclamation("ABCDE")