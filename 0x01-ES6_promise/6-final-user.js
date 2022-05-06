import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const myObjs = await Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((values) => values);

  const error = String(myObjs[1].reason);
  delete myObjs[1].reason;
  myObjs[1].value = error;
  console.log(myObjs);
  return myObjs;
}
