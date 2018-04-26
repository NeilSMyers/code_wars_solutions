//Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
//The output should be two capital letters with a dot seperating them.
//It should look like this:
//Sam Harris => S.H
//Patrick Feeney => P.F


function abbrevName(name){
  return (name.split(' ')[0].split('')[0] + "." + name.split(' ')[1].split('')[0]).toUpperCase();
 }
 
 console.log(abbrevName("sam harris"))//, "S.H");
 console.log(abbrevName("Patrick Feenan"))//, "P.F");
 console.log(abbrevName("Evan cole"))//, "E.C");
 console.log(abbrevName("P Favuzzi"))//, "P.F");
 console.log(abbrevName("david Mendieta"))//, "D.M");