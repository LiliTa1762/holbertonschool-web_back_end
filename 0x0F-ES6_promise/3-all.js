import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const resolvedPromisesArray = [uploadPhoto(), createUser()];
  return Promise.all(resolvedPromisesArray)
    .then((val) => console.log(`${val[0].body} ${val[1].firstName} ${val[1].lastName}`))
    .catch(() => Error(console.log('Signup system offline')));
}
