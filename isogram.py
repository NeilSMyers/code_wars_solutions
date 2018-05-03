# Check to see if each word is an isogram

def isogram(word):
  arr = []
  for x in word.lower():
    if x == " " or x == "-":
      x.replace(x,'')
    else:
      arr.append(x)
  if len(arr) > len(set(arr)):
    print(False)
  else:
    print(True)
      
isogram("lumberjacks")
isogram("isogram")
isogram("people")
isogram("hello")
isogram("hi-ae-jq")
isogram("hi ae jq")