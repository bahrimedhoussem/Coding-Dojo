  import "./App.css";
  import PersonCard from "./components/personcard";
  


  function App() {
    const peopleArr = [
      {
        firstName: "Doe",
        lastName: "Jane",
        age: 45,
        hairColor: "Black",
      },
      {
        firstName: "Smith",
        lastName: "John",
        age: 88,
        hairColor: "Brown",
      },
    
    ];
    return (
      <div className = "App">
        
      {peopleArr.map ((personKey) => (
        
      
      <PersonCard 
        
        firstName={personKey.firstName}
            lastName={personKey.lastName}
            age={personKey.age}
            hairColor={personKey.hairColor}
            
          />
          
          ))}
    
          
      </div>
    );
  }




  export default App;
