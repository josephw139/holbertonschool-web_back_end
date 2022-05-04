export default function getResponseFromAPI() {
  let promise = new Promise(function(resolve, reject) {
    resolve(true);

    reject(new Error("…")); // ignored
    setTimeout(() => resolve("…")); // ignored
  });

    return promise;
}
