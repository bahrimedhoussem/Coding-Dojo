import {BrowserRouter,Routes , Route } from 'react-router-dom'
import NumberId from './components/Id'; 
import Home from './components/Home';
import Hello from './components/WordHello';
import Color from './components/Color';
import React from 'react';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route  path = '/:id' element = {<NumberId/>} />
        <Route  path = '/:hello' element = {<Hello/>} />
        <Route  path = '/home'  element = {<Home/>} />
        <Route path = '/:word/:color1/:color2' element ={<Color/>}/>
      </Routes>
    </div>
  );
}

export default App;
