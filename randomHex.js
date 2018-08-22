// Write a JavaScript program to generate a random hexadecimal color code

function randomHex() {
  const hex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'];
  const randHex = [];
  for(let i=0; i < 6; i++ ) {
    randHex.push(hex[Math.floor(Math.random() * hex.length)]);
  }
  return(randHex.join(""));
}

console.log(randomHex());