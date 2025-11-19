// Explain promises?
(`A promise is an object used to handle asynchronous operations,
Promises Provide a clear way to work with asynchronous code campare to callback,
they represent a value that may be available now or future or never`)


const myPromise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Task completed!");
  } else {
    reject("Something went wrong!");
  }
});

myPromise
  .then(result => console.log(result))
  .catch(error => console.log(error));