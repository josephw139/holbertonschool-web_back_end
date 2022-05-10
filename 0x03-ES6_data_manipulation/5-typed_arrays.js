export default function createInt8TypedArray(length, position, value) {
  let buff = new ArrayBuffer(length)
  let int8 = new Int8Array(buff);
  int8[position] = value;

  return new DataView(buff);
}