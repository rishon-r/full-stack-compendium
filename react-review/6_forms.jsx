// FORMS and CONTROLLED COMPONENTS in REACT

// FORMS and CONTROLLED COMPONENTS in REACT

/*
The core tension: remember from the DOM guide that an <input> maintains its own internal, live value the moment
 the user types — the browser does this automatically, with zero JavaScript needed. React's philosophy is declarative: 
 the UI should always reflect your data/state, not manage its own hidden internal state that you have to go "ask" for later.
  Forms are the one place these two philosophies collide, and React resolves it with the controlled component pattern
*/

// EXAMPLE (with single field)
import { useState } from 'react';

function NameForm() {
  const [name, setName] = useState('');

  function handleChange(event) {
    setName(event.target.value); // update state every keystroke
  }

  function handleSubmit(event) {
    event.preventDefault(); // stop the browser's default full-page reload on submit
    console.log('Submitted name:', name);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}       // input's displayed value is FORCED to match state
        onChange={handleChange} // every keystroke updates state
      />
      <button type="submit">Submit</button>
    </form>
  );
}
/*
Walk through what actually happens on each keystroke:

User types a character into the input.
The browser's native behavior would normally just update the input's internal .value property immediately (per the DOM guide's Section 4/9).
But because you gave it a React-controlled value={name}, React's onChange handler fires first, calling setName(event.target.value).
setState triggers a re-render. The component function runs again, name is now the new character, and the JSX re-renders <input value={name} /> with that new value.
The net visual effect looks identical to the browser just updating the input normally — but the actual value now lives in your React state, not hidden inside the DOM node.
*/

// EXAMPLE (with multiple fields)
// Typical to use objects here instead of separate state variables
function SignupForm() {
  const [formData, setFormData] = useState({ email: '', password: '' });

  function handleChange(event) {
    const { name, value } = event.target; // uses the input's `name` attribute
    setFormData(prev => ({ ...prev, [name]: value })); // spread old state, overwrite one field
  }

  return (
    <form>
      <input name="email" value={formData.email} onChange={handleChange} />
      <input name="password" type="password" value={formData.password} onChange={handleChange} />
    </form>
  );
}

// CHECKBOXES AND SELECTS
/*
EXAMPLE:

const [isChecked, setIsChecked] = useState(false);
const [country, setCountry] = useState('US');

<input type="checkbox" checked={isChecked} onChange={e => setIsChecked(e.target.checked)} />

<select value={country} onChange={e => setCountry(e.target.value)}>
  <option value="US">United States</option>
  <option value="CA">Canada</option>
</select>

*/

// NOTE ON preventDefault()
// By default, submitting an HTML <form> triggers a full browser page reload/navigation — 
// the classic pre-JavaScript web behavior. In a React app (a single-page app that manages its own state in memory),
// a full reload would wipe out everything. event.preventDefault() inside your onSubmit handler stops that default browser 
// behavior so your React code stays in control of what happens next — usually sending the data somewhere with fetch() instead of
// letting the browser navigate away.

// UNCONTROLLED COMPONENTS (Not generally idiomatic)
// By default, submitting an HTML <form> triggers a full browser page reload/navigation —
//  the classic pre-JavaScript web behavior. In a React app (a single-page app that manages its own state in memory),
// a full reload would wipe out everything. event.preventDefault() inside your onSubmit handler stops that default browser behavior 
// so your React code stays in control of what happens next — usually sending the data somewhere with fetch() instead of letting the 
// browser navigate away.
import { useRef } from 'react';

function UncontrolledForm() {
  const nameRef = useRef(null);

  function handleSubmit(event) {
    event.preventDefault();
    console.log(nameRef.current.value); // reach into the real DOM node directly
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" ref={nameRef} />
      <button type="submit">Submit</button>
    </form>
  );
}