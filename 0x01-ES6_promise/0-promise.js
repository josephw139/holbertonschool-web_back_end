export default function getResponseFromAPI() {
  const promise = new Promise(((resolve, reject) => {
    resolve(true);

    reject(new Error('…')); // ignored
    setTimeout(() => resolve('…')); // ignored
  }));

  return promise;
}
