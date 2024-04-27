
import './App.css';
import react , {useState} from 'react'
function App() {
  const [pokemons , setPokemons] = useState([]);
    const fetchPokemon = ()=>{
      fetch ("https://pokeapi.co/api/v2/pokemon")
        .then(response => {
          return response.json();
        }).then(response => {
          console.log(response);
          const data = response.results 
          setPokemons(data)
        })
      
        .catch(err =>{
          console.log(err);
        });
      
    
    }
    return (
      <div className="App">
      
        <button onClick = {fetchPokemon}>Fetch Pokemno</button>

        <ul>
        {pokemons.map((pokemon , index) => (
          <li key = {index}>
            {pokemon.name}
          </li> 
          ))}

        </ul>
      
      </div>
  );
}

export default App;
