export default function hasValuesFromArray(set, array) {
  let flag = true;
  array.map((ele) => {
    if (!(set.has(ele))) {
      flag = false;
    }
    return flag;
  });
  return flag;
}
