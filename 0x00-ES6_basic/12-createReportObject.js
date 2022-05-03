export default function createReportObject(employeesList) {
  const myObject = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length;
    },
  };

  return myObject;
}
