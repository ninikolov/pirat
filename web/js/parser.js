// text module
var fs = require('fs');

// break lines into strings array
var strings = fs.readFileSync('snitch.txt').toString().split("\n");
var  tokens = [];

// create new array with phoenetic parts
for(i in strings) {
	tokens[i] = strings[i].split(">");
}

// word to guess is chosen randomly
var randWordNum = Math.floor(Math.random() * (tokens.length));
var randWord = tokens[randWordNum][0];

// #phoenetic parts
// == #divs to create in html
var numCols = tokens[randWordNum].length-1;

// bootstrap length = 12
// dont make 5
// magic
// <div class="col-md-colLength
var colLength = 12/numCols;


console.log(tokens);
console.log(randWord);
console.log(numCols);
console.log(colLength);
