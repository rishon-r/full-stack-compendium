// STATE MANAGEMENT - creating dynamic components
// State refers to data that a component owns that can change over time
// When state of a component changes, React re renders it in order to reflect the new value
// State is how a component remembers things (like form input, a counter, or a toggle) across re renders
// and it is what defines what a UI displays over any given moment

// HOOKS
// A hook is a special react function
// It allows components access to special React features - like state or life cycle behaviour 
// These were previously only available in class components which Hooks have made legacy now
// Hooks must be called inside a function's top level, not inside loops, conditions or nested functions

// THE useState HOOK
// useState is a React hook that gives a component a piece of state that PERSISTS across re renders
// Calling useState(initialValue) returns an array with two items:
// (i) The current value
// (ii) The setter function to update it
// Calling the setter with a new value triggers a re render with a new value
// NOTE: it is VERY IMPORTANT that you do not change the value of the state value directly without calling the setter
// The only way to change the state value is through the setter
// i.e STATE IS IMMUTABLE

// CODE EXAMPLE
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0); // initial value: 0

  function increment() {
    setCount(count + 1); // updates state, triggers re-render
  }

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Add one</button>
    </div>
  );

}

// THE prev PARAMETER
// prev is a parameter name used in the "functional updater" form of the state setter function
// Instead of passing a new value as a parameter to the setter, you pass directly a function
// that receives the current state as its argument and returns the new state
// This is safer when the new value of the state depends upon the previous value


import { useState } from 'react';

function PrevExample() {
  const [count, setCount] = useState(0);

  function incrementTwice() {
    setCount(prev => prev + 1); // uses actual current value
    setCount(prev => prev + 1); // uses actual current value again
    // Result: count increases by 2
    /*
    Why this works:

    Instead of handing setCount a number (computed right now, 
    from a possibly-stale closure), you hand it a function. React doesn't run that function immediately either — it queues it
    Internally, React maintains something like a small queue of pending updates for count
    It runs all the functions in the queue right before the re render
    This is called batching.
    React intentionally waits until the whole synchronous block of code (your event handler) is finished before doing any actual 
    re-rendering — rather than re-rendering after every single setCount call individually.
    This is a deliberate performance optimization: two calls to setCount in the same handler produce one re-render, not two

    */
  }

  function brokenIncrementTwice() {
    setCount(count + 1); // both calls use the SAME stale `count`
    setCount(count + 1); // Result: count only increases by 1
    /*
    Why is this broken: 

    Both calls to setCount(count + 1) reference the exact same count variable — 
    the one captured when this render's brokenIncrementTwice function was created. Even though you called setCount twice,
    both calls compute count + 1 using the same starting number. If count was 0, both lines literally compute setCount(0 + 1) —
    twice. So you're not "adding 1, then adding 1 to the new total" — you're "setting it to 1, then setting it to 1 again."
    */
  }

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={incrementTwice}>Increment twice (correct, +2)</button>
      <button onClick={brokenIncrementTwice}>Increment twice (broken, +1)</button>
    </div>
  );
}

// THE useEffect HOOK - Side effects in react

// What are SIDE EFFECTS?
// A side effect is essentially code that interacts with something outside the render itself

// Why does useEffect matter?
// During rendering, React is completely focused on calculating what the UI should look like.
//  If you try to fetch data from an API or set a timer directly inside the main body of your component, 
// it would happen during rendering. This can cause endless re-rendering loops, freeze your web page, or make your app feel laggy

// How useEffect() works
// It takes two arguments: (i) a function (called THE EFFECT), (ii) a DEPENDENCY ARRAY (optional argument)
// The function is what runs the desired side effect
// The dependency array controls when the effect reruns 
// How and when your useEffect runs depends entirely on what you pass as the second argument
// There are mainly three scenarios based on what is provided as the dependency array:
// 1. [] — runs once, after the first render only
// 2. omitted entirely — runs after every render
// 3. Runs when a specific state or prop changes: thos props/states should be listed as elements of the dependency array


import { useState, useEffect } from 'react';

function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data));
  }, [userId]); // dependency array, runs every time userId changes

  return <div>{user ? user.name : 'Loading...'}</div>;
}

// CLEAN UP FUNCTION
/*
A cleanup function in useEffect is React's mechanism for tidying up after a side effect when a component updates or disappears from the screen.

If a side effect establishes an ongoing background operation—such as a timer, event listener,
or WebSocket connection—it will continue running in the browser's memory even if the component is removed.
A cleanup function cancels those background tasks to prevent memory leaks and unexpected bugs

To use a cleanup function, return a function from inside your useEffect callback, example: 
useEffect(() => {
  // 1. Setup phase: runs when the component mounts (or dependencies update). 
  console.log("Setting up effect");

  return () => {
    // 2. Cleanup phase: runs when the component unmounts (or before re-running setup). 
    // Unmounting means whn the component is removed from DOM like when you navigate to a new page
    // Before re-running the effect: If the dependency array triggers a re-run because a state variable changed,
    // React runs the cleanup function for the previous state first, before running the setup function for the new state
    console.log("Cleaning up effect");
  };
}, [dependency]);

*/

// COMMON MISTAKES
// 1. Using a state variable in the effect but not including it as a dependency
// 2. Having an object in your dependency (because objects are references and this will cause an effect to run on every re render)