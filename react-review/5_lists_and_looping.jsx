// LISTS & LOOPING - RENDERING DYNAMIC DATA

// ARRAY MAPPING
// Each <li> gets a key, using the item's index in the array (0, 1, 2). 
// React needs this to track which list item is which across re-renders — it's not rendered visibly,
// it's purely for React's internal bookkeeping
// The key attribute exists to solve one specific problem: when a list re-renders,
//  how does React know which element in the new list corresponds to which element in the old list?
// key gives each element in a list a stable identity that persists across renders, so React can match old elements to new ones
//  by identity rather than by guessing from position

/*
BETTER EXPLANATION:

React renders UI as a function of state. State changes trigger re-renders: the component function reruns,
producing a new virtual DOM tree, which React diffs against the old one and applies minimal real DOM updates.
Components are functions returning JSX; props flow down (read-only), state is owned locally and changed only via setters.
Parent re-renders cascade to children by default, even without prop changes. 

keys are used during the diffing step, right after a state change, to match old elements to new elements by identity rather than position —
and that matching decision is what determines, during the actual DOM update, which real DOM nodes get reused-and-patched,
which get deleted, and which get freshly created

*/
function FruitList(){
    const fruits = ["Apple", "Banana", "Orange"]

    return(
        <ul>
           {fruits.map( (fruit, index) => (
                <li key={index}>{fruit}</li>
            )) }
        </ul>
    );
}

// It is actually a better practice to use a unique id as the key instead of an index
// It is a bad practice to make index the key
// EXAMPLE
function UserList() {
    const users = [
        { id: 1, name: 'Alice'},
        { id: 2, name: 'Bob'},
        { id: 3, name: 'Charlie'}
    ]

    return(
        <ul>
            { users.map((user) => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    )
}

// DYNAMIC LIST WITH ADD/REMOVE (An example)

import { useState } from "react";

function DynamicList() {
  const [items, setItems] = useState([
    { id: 1, text: "Buy groceries" },
    { id: 2, text: "Walk the dog" },
    { id: 3, text: "Finish report" },
  ]);
  const [inputValue, setInputValue] = useState("");

  function handleAdd() {
    if (inputValue.trim() === "") return; // ignore empty input

    const newItem = {
      id: Date.now(), // simple way to get a unique id
      text: inputValue,
    };

    // Never mutate state directly (e.g. items.push(newItem)) —
    // always create a NEW array so React detects the change.
    setItems([...items, newItem]);
    setInputValue(""); // clear the input after adding
  }

  function handleRemove(idToRemove) {
    // filter() returns a new array, excluding the removed item —
    // again, never mutate the original array in place.
    setItems(items.filter((item) => item.id !== idToRemove));
  }

  return (
    <div>
      <input
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Add a new item"
      />
      <button onClick={handleAdd}>Add</button>

      <ul>
        {items.map((item) => (
          // key={item.id} — stable identity, NOT the array index,
          // since items can be removed from anywhere in the list.
          <li key={item.id}>
            {item.text}
            <button onClick={() => handleRemove(item.id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

