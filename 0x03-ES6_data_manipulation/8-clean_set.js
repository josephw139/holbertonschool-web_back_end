export default function cleanSet(set, startString) {
  let result = '';

  if (startString === '' || typeof startString !== 'string') {
    return '';
  }

  set.forEach((ele) => {
    if (ele.startsWith(startString)) {
      result += (ele.split(startString)[1] + '-');
    }
  });

  return result.slice(0, -1);
}
