// Write a JavaScript program to get every nth element in an given array. (nth usually represents an argument number, so pass in an array, and a number for how many elements to skip. IE 2, or 3, etc.)
function arraySkip(arr, interval){
  const result = [];
  for (let i = 0; i < arr.length; i += interval) {
    result.push(arr[i]);
  }
  return result;
}
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(arraySkip(arr, 2));