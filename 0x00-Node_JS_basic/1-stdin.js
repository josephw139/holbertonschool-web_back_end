// user input

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.setPrompt(`Welcome to Holberton School, what is your name?\n`);
readline.prompt();

readline.on('line', function(line) {
  console.log(`Your name is: ${line}`);
  readline.close();
}).on('close', function() {
  console.log('This important software is now closing');
});