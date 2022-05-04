export default function handleResponseFromAPI(promise) {
  const statusObj = {
    status: 200,
    body: 'success',
  };
  return promise.then(statusObj).catch(new Error()).finally(console.log('Got a response from the API'));
}
