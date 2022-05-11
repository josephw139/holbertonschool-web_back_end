export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const int8 = new Int8Array(buff);
  int8[position] = value;

  return new DataView(buff);
}
