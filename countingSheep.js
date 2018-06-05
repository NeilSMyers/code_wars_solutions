var countSheep = function (num) {
  let arr = [];
  for (i = 1; i <= num; i++) {
    arr.push(`${i} sheep...`)
  }
  return arr.join('')
}

countSheep(1)//, "1 sheep...");
countSheep(2)//, "1 sheep...2 sheep...");
countSheep(3)//, "1 sheep...2 sheep...3 sheep...");