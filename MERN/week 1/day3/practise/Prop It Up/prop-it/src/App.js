import React from 'react';

import PersonCard from './components/PersonCard'; 






function App() {
  
    
      const people = [
        {firstName : "Doe" , lastName : "jane"  , age : 45 , hairColor : "black"}, 
        {firstName :  "Smith"  , lastName :  "john" , age : 88 , hairColor : "brown"},
        {firstName :  "Fillmore"  , lastName :  "Millard" , age : 50 , hairColor : "brown" },
        {firstName :  "Smith"  , lastName :  "Maria" , age : 62 , hairColor : "brown" },
        
      ]; 

        return people.map( item => (`<h1>${item.firstName} , ${item.lastName} </h1>`) ) ,
              people.map( item => `<h1>${item.age} `  ) ,
              people.map( item => `<h1>${item.hairColor} `  );
        

}

export default App;
