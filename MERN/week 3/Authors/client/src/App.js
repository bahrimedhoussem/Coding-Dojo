import logo from './logo.svg';
import './App.css';
import {Routes , Route} from 'react-router-dom'
import List from './components/List';
import Create from './components/create';
import Update from './components/update';



function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/authors" element={<List />} />
        <Route path="/authors/new" element={<Create/>} />
        <Route path="/authors/:id/edit" element={<Update />} />
      </Routes>
    </div>
  );
}

export default App;
