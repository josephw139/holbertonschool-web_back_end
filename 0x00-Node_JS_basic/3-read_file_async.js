// Reading a file synchronously with Node JS

const fs = require('fs');

const countStudents = async (file) => {
  let db;
  try {
    db = await fs.promises.readFile(file, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const data = [];
  const rows = db.split('\n');

  rows.forEach((row) => {
    if (row.length > 0) {
      data.push(row.split(','));
    }
  });

  const cs = [];
  const swe = [];
  data.forEach((row) => {
    if (row.includes('CS')) {
      cs.push(row[0]);
    }
    if (row.includes('SWE')) {
      swe.push(row[0]);
    }
  });
  console.log(`Number of students: ${data.length - 1}`);
  console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
  console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);

  return [data, cs, swe];
};

module.exports = countStudents;
