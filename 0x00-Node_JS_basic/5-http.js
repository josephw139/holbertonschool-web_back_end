// http server

const http = require('http');
const process = require('process');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  if (req.url == '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (req.url == '/students') {
    res.write('This is the list of our students\n');
    await countStudents(process.argv[2]).then((values) => {
      res.write(`Number of students: ${values[0].length - 1}\n`);
      res.write(`Number of students in CS: ${values[1].length}. List: ${values[1].join(', ')}\n`);
      res.write(`Number of students in SWE: ${values[2].length}. List: ${values[2].join(', ')}`);
    }).catch(() => {
      res.write(`This is the list of our students\nCannot load the database`);
      res.end();
    });
    res.end();
  }
}).listen(1245);

module.exports = app;
