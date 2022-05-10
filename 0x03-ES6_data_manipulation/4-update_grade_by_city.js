export default function updateStudentGradeByCity(students, city, newGrades) {
  let newList = students.filter(ele => ele['location'] === city);

  return newList.map(myFunction);

  function myFunction(student) {
    let grade = newGrades.filter(ele => ele['studentId'] === student['id'])

    try {
      student['grade'] = grade[0]['grade'];
    } catch {
      student['grade'] = 'N/A'
    }

    return student;
  }
}