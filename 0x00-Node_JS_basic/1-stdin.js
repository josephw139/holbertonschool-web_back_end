// user input

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
    let line = process.stdin.read();
    if (line) {
      process.stdout.write(`Your name is: ${line}`);
    }
  }).on('end', () => {
    process.stdout.write('This important software is now closing\n');
  });
