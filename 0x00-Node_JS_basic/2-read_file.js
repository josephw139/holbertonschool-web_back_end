// Reading a file synchronously with Node JS

const fs = require("fs");

function countStudents(path) {
  let data = [];

  if (!(fs.existsSync(path))) {
    throw new Error('Cannot load the database');
  }
  const db = fs.readFileSync(path, 'utf8');

  let rows = db.split('\n');

  rows.forEach(row => {
    if (row.length > 0) {
      data.push(row.split(','));
    }
  })

  let cs = [];
  let swe = [];
  data.forEach(row => {
    if (row.includes('CS')) {
      cs.push(row[0]);
    }
    if (row.includes('SWE')) {
      swe.push(row[0]);
    }
  })
  console.log(`Number of students: ${data.length - 1}`);
  console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
  console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
}

module.exports = countStudents;
