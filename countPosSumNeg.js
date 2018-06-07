// Return a count of positive integers in array and sum negative integers

function countPositivesSumNegatives(input) {
  let pos = 0
  let neg = 0
  let arr = []
  if (input == 0 || input == null) {
    return []
  } 
  for (i = 0; i < input.length; i++) {
    if (input[i] > 0) {
      pos += 1
    } else {
      neg += input[i]
    }
  }
  arr.push(pos)
  arr.push(neg)
  return arr
}

countPositivesSumNegatives([1, 2, 3, 4, -11, -12])// [4, -23]