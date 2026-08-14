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
