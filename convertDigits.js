// Write a JavaScript program to converts a specified number to an array of digits

function convertDigits(num) {
  let arr = num.toString().split('')
  return arr.map(Number)
}

console.log(convertDigits(1234556))