export default function createReportObject(employeesList) {
    myObject = {
	allEmployees: employeesList,
	getNumberOfDepartments(employeesList) {
	    return Object.keys(employeesList).length;
	}
    }
}
