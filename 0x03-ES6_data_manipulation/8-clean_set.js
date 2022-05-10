export default function cleanSet(set, startString) {
  let result = '';
  let arr = Array.from(set);

  if (startString === '') {
    return '';
  }

  arr.map(ele => {
    if (ele.startsWith(startString)) {
      result += (ele.split(startString)[1] + '-');
    }
  });

  return result.slice(0, -1);
}