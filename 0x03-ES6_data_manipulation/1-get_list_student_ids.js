export default function getListStudentIds(array) {
  if (Array.isArray(array) === false) {
    return [];
  }

  function id(element) {
    return element.id;
  }

  const idList = array.map(id);

  return idList;
}
