import React, { useState } from 'react';
import './App.css'; // Assuming your CSS file exists
import BoxDisplay from './components/BoxDisplay';

function App() {
  const [box, setBox] = useState('');
  const [bar, setBar] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    setBar([...bar, box]);
    setBox('');
  };

  return (
    <div className="App">
      <form className="form" onSubmit={handleSubmit}>
        <h1>Color</h1>
        <input type="color" onChange={(e) => setBox(e.target.value)} />
        <button>Add</button>
      </form>

      <BoxDisplay boxes={bar} />
    </div>
  );
}

export default App;





