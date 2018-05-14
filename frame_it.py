#print out each string framed in asterics

def frame_it_yo(string):
  top_bottom = []
  words = string.split()
  for word in words:
    top_bottom.append(len(word))
  longest_word = max(top_bottom)
  print("*" * (longest_word + 4))
  for word in words:
    print("* "+word+(" "*(longest_word-len(word)+1))+"*")
  print("*" * (longest_word + 4))

frame_it_yo('Hello World in a frame')
frame_it_yo("Anything indubitably framed")
frame_it_yo("supercalafradgulisticexpialadocious")
