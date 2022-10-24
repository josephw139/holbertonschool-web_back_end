// Student Controller
import readDatabase from '../utils';


class StudentsController {

  static getAllStudents(request, response) {
    response.status(200);
    readDatabase(process.argv[2]).then(values => {
      response.write(`Number of students: ${values[0].length - 1}\n`);
      response.write(`Number of students in CS: ${values[1].length}. List: ${values[1].join(', ')}\n`);
      response.write(`Number of students in SWE: ${values[2].length}. List: ${values[2].join(', ')}`);
      response.end();
    })
  }

  static getAllStudentsByMajor(request, response) {
    response.status(200);
    const major = request.params;
    if (major.major != 'CS' && major.major != 'SWE') {
      response.status(500);
      response.write('Major parameter must be CS or SWE');
      response.end();
      return;
    }
    readDatabase(process.argv[2]).then(values => {
      let num;
      if (major.major == 'CS') {
        num = 1;
      } else {
        num = 2;
      }
      response.write(`List: ${values[num].join(', ')}`);
      response.end();
    })
  }
}

module.exports = StudentsController;
