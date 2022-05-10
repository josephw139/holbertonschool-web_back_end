export default function getListStudentIds(array) {
  if (Array.isArray(array) === false) {
    return [];
  }

  let idList = array.map(id);

  function id(element) {
    return element['id'];
  }

  return idList;
}