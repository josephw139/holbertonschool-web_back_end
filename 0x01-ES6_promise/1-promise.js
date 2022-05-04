export default function getFullResponseFromAPI(success) {
  if (success === true) {
    const myObj = {
      status: 200, body: 'Success',
    };
    return Promise.resolve(myObj);
  }
  return Promise.reject(new Error('The fake API is not working currently'));
}
