// PROMISES
// Promises are a better way to handle asynchronous code
// Promises let us run code in response to an asynchronous operation finishing, without blocking the rest of the program while we wait
// A Promise in JavaScript represents a value that may be available now, later, or never.
// It is used to handle asynchronous operations like fetching data from a server.
// A Promise can be in one of three states: pending, fulfilled (success) or rejected (failed)
// When creating a promise manually, it is created alongside aan executor function that is mentioned inside the promise's parentheses
// This executor takes two arguments: resolve and reject
// resolve is called when a promise is fulfilled and reject is called when it is not
// They are both called with data that is then returned back
// A promise is also followed by methods .then() and .catch()
// The .then block contains a function that is executed when the promise succeeds and takes the first argument as the result returned by the resolve
// Multiple then blocks can follow each other 
// a .catch block is used after all the end blocks and is used when an error occurs in one of the promises resulting in a reject
// It also takes one argument which is the message returned by the reject
// then, at the end is a .finally block which contains code that runs regardless, after all .then or .catch have been executed
// As promises are used to handle async code, the function inside a promise usually corresponds to an async task such as a write to a database
// or fetch from an API

// Let's create a basic Promise:
const myPromise = new Promise((resolve, reject) => {
  // Simulate an asynchronous operation like fetching data from an API
  setTimeout(() => {
    const success = true;

    if (success) {
      resolve("Data fetched successfully!"); // If successful, call resolve with some value
    } else {
      reject("Something went wrong!"); // If there's an error, call reject
    }
  }, 1000); // Wait for 1 second
});

// We can consume the Promise like this:
myPromise.then((result) => {
  // This runs if resolve() is called
  console.log(result); // Output: "Data fetched successfully!"
}).catch((error) => {
  // This runs if reject() is called
  console.error(error);
});

// The key reason we use promises for execution of asynchronous code is that the other option is using multiple nested callback functions
// Using multiple nested callback functions results in code that is hard to read and debug

// Callback Hell Example (not ideal - hard to read and debug):
function fetchData(callback) {
  setTimeout(() => {
    console.log("Data fetched");
    callback();
  }, 1000);
}

function processData(callback) {
  setTimeout(() => {
    console.log("Data processed");
    callback();
  }, 1000);
}

function displayData() {
  setTimeout(() => {
    console.log("Data displayed");
  }, 1000);
}

// Nested callbacks become hard to manage and debug (Callback Hell)
fetchData(() => {
  processData(() => {
    displayData();
  });
});

// Promises make the flow much cleaner and readable
function fetchDataPromise() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Data fetched");
      resolve();
    }, 1000);
  });
}

function processDataPromise() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Data processed");
      resolve();
    }, 1000);
  });
}

function displayDataPromise() {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log("Data displayed");
      resolve();
    }, 1000);
  });
}

// Promise chaining improves readability and avoids deeply nested code
fetchDataPromise()
  .then(processDataPromise)
  .then(displayDataPromise);

// Why do we need to nest callback functions in the first place?

// In JavaScript, many operations (like I/O, network requests, timers) are asynchronous.
// That means they don't return immediately—they take time to complete.

// To ensure one async task runs AFTER another, we used to nest callbacks.
// This is called "sequencing" asynchronous operations using callbacks.

function stepOne(callback) {
  setTimeout(() => {
    console.log("Step 1 done");
    callback();
  }, 1000);
}

function stepTwo() {
  console.log("Step 2 done");
}

stepOne(() => {
  stepTwo(); // This runs only after Step 1 is complete
});

// More on the resolve() function

// When we create a Promise, we pass it a function with two parameters: resolve and reject
// Calling resolve() tells the Promise that the operation succeeded.
// You can pass any data type to resolve(): string, number, object, array, even another Promise.

const myResolvedPromise = new Promise((resolve, reject) => {
  const user = { name: "Rishon", age: 25 };

  // Resolving the Promise with an object
  resolve(user);
});

myResolvedPromise.then((userData) => {
  // The argument passed to resolve() is received here
  console.log("User's name is", userData.name); // Output: "User's name is Rishon"
});

// More on the .then() method

// The .then() method is used to handle the result of a resolved Promise
// It takes a function that receives the resolved value of the Promise

const greet = new Promise((resolve) => {
  resolve("Hello from the Promise!");
});

greet.then((message) => {
  console.log(message); // Output: "Hello from the Promise!"
});

// Promise.all() takes an array of Promises and returns a new Promise.
// This new Promise resolves when ALL of the input Promises resolve.
// It rejects immediately if ANY of them reject.

const p1 = new Promise((resolve) => setTimeout(() => resolve("First"), 1000));
const p2 = new Promise((resolve) => setTimeout(() => resolve("Second"), 2000));
const p3 = new Promise((resolve) => setTimeout(() => resolve("Third"), 1500));

Promise.all([p1, p2, p3]).then((results) => {
  console.log(results); // Output: ["First", "Second", "Third"]
}).catch((error) => {
  console.error("One of the promises failed", error);
});

// VISUAL DIAGRAM
/*
┌────────────────────────────┐
│     Promise Created        │
│ (new Promise(resolve, reject)) │
└────────────┬───────────────┘
             │
             ▼
     Initial State: "pending"
             │
   ┌─────────┴──────────┐
   │                    │
   ▼                    ▼
resolve(value)     reject(reason)
   │                    │
   ▼                    ▼
State: "fulfilled"   State: "rejected"
   │                    │
   ▼                    ▼
 .then() gets value    .catch() gets reason
   │                    │
   ▼                    ▼
  Success!          Handle error!
*/

// Example code version:

const myNewPromise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Data loaded");   // moves to fulfilled
  } else {
    reject("Failed to load"); // moves to rejected
  }
});

// The .then() method runs if the Promise is fulfilled
myNewPromise
  .then((data) => {
    console.log("Then block:", data);
  })
  .catch((error) => {
    // The .catch() method runs if the Promise is rejected
    console.error("Catch block:", error);
  });


// More on the .catch() method
// .catch() is a method on a Promise that allows you to handle errors (i.e., rejections) that occur during the execution of asynchronous code.
// It’s the Promise equivalent of a try/catch block.
// Example Syntax:
/*
somePromise()
  .then(result => {
    // handle result
  })
  .catch(error => {
    // handle error
  });
*/
// Working example

/*
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    console.log('Data:', data);
  })
  .catch(error => {
    console.error('Something went wrong:', error);
  });

*/

// AN EXAMPLE OF HOW REJECT WORKS WITH PROMISES:
function getUser(id) {
  return new Promise((resolve, reject) => {
    if (id === 0) {
      reject(new Error("Invalid user ID"));
    } else {
      resolve({ id, name: "Rishon" });
    }
  });
}

getUser(0)
  .then(user => {
    console.log("User found:", user);
  })
  .catch(err => {
    console.error("Promise rejected:", err.message);
  });
