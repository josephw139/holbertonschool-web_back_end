/* eslint-disable no-unused-vars */
export default function appendToEachArrayValue(array, appendString) {
  const appArray = [];
  for (const idx of array) {
    appArray.push(appendString + idx);
  }

  return appArray;
}
