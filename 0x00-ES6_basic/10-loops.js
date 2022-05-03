/* eslint-disable no-unused-vars */
export default function appendToEachArrayValue(array, appendString) {
  for (let idx of array) {
    idx += appendString;
  }

  return array;
}
