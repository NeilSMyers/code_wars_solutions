//You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

function getMiddle(s) {
  var x = s.split("")
  for (i = x.length; i > 2; i -= 2) {
    x.pop()
    x.shift()
  }
  return x.join("")
}

console.log(getMiddle("test"))//,"es");
console.log(getMiddle("testing"))//,"t");
console.log(getMiddle("middle"))//,"dd");
console.log(getMiddle("A"))//,"A");