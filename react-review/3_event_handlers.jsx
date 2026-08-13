// EVENT HANDLERS
// Event handlers are how your components respond to things the user does — clicks, typing, submitting a form, hovering, etc. 
// Let's go through how they work and the rules around them

// BASIC PATTERN
// You attach a handler by passing a function to a camelCase event prop, like onClick, onChange, onSubmit
// EXAMPLE
function Button() {
  function handleClick() {
    alert("Button was clicked!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
// Two details matter here
// 1. camelCase, not lowercase. HTML uses onclick; JSX uses onClick. 
// Same for onchange → onChange, onsubmit → onSubmit, and so on — this matches JavaScript naming conventions rather than HTML's.
// 2. Pass the function itself, not a call to it. onClick={handleClick} passes the function so React can call it later, when the click actually happens. 
// onClick={handleClick()} would call it immediately during render — which is a very common bug

// INLINE HANDLER
// You don't need a separate named function — an arrow function inline works too, and is common for short handlers or when you need to pass arguments:
// Example: <button onClick={() => alert("Clicked!")}>Click me</button>

// This is also the standard way to pass an argument to a handler, since onClick={handleDelete(id)} would call it immediately (same bug as above):
// E.g.
/*

function TodoItem({ id, text, onDelete }) {
  return (
    <li>
      {text}
      <button onClick={() => onDelete(id)}>Delete</button>
    </li>
  );
}

*/

// EVENT PARAMETER
// Whatever name you give the first parameter of a handler function, React always fills it in with the event object when it calls your handler
// EXAMPLE:
/*
function handleClick(event) {
  console.log(event);
}

<button onClick={handleClick}>Click</button>
*/
// You can name that parameter anything — event, e, evt — it's just a regular function parameter. e is the common convention. 
// This parameter is implicit: you never write it in the JSX itself; React supplies it automatically when the event fires
// The tricky part is when you also want to pass your own data — like an item's id — into the handler. 
// (See below example)
/*
function handleDelete(id) {
  console.log("Deleting item", id);
}

<button onClick={() => handleDelete(id)}>Delete</button>

*/
// Since onClick={handleDelete(id)} would call handleDelete immediately during render (not on click), 
// you wrap it in an arrow function instead
// Here, () => handleDelete(id) is the actual function passed to onClick. React calls that function on click — with no arguments —
// and its body then calls handleDelete(id) using the id it captured from the surrounding scope

// Combining both your parameter and the event object
// If you need both your own data and the event object, just accept both in the wrapper — 
// the event object still arrives automatically as the argument to the arrow function itself
// VERY IMPORTANT EXAMPLE (Accepting both event object and your parameter in the wrapper)
/*
function handleDelete(id, event) {
  event.preventDefault();
  console.log("Deleting item", id);
}

<button onClick={(e) => handleDelete(id, e)}>Delete</button>
*/