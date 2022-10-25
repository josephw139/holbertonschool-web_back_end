// express server

const express = require('express');
const app = express();
const process = require('process');
const countStudents = require('./3-read_file_async');

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
    await countStudents(process.argv[2]).then(values => {
      res.write(`Number of students: ${values[0].length - 1}\n`);
      res.write(`Number of students in CS: ${values[1].length}. List: ${values[1].join(', ')}\n`);
      res.write(`Number of students in SWE: ${values[2].length}. List: ${values[2].join(', ')}`);
    })
    res.end();
})

app.listen(1245);

module.exports = app;
