// fetch() is a built-in function to make HTTP requests from the browser
// Note that the type of request fetch makes is a 'GET' request
// It returns a Promise that resolves to the Response object of the request

// Basic fetch example
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => {
    // First we need to convert the raw response to JSON
    return response.json();
  })
  .then((data) => {
    // Now we can use the actual data from the response
    console.log("Post title:", data.title);
  })
  .catch((error) => {
    // If the fetch fails (e.g., no internet), this block runs
    console.error("Error fetching data:", error);
  });

/*
  How fetch() works:
    1. It makes a network request.
    2. Returns a Promise.
    3. That Promise resolves to a Response object.
    4. You convert it using response.json(), which also returns a Promise.
    5. Then you use the data.

  Note: fetch() does not reject on HTTP errors (like 404); it only rejects on network failure.
*/