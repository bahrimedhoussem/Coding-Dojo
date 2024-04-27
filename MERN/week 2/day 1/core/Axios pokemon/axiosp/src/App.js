import {useState} from 'react'
import axios from 'axios'


function App() {
  const [pokemons , setPokemons] = useState([]);
    const axiosPokemon = ()=>{
      axios.get('https://pokeapi.co/api/v2/pokemon').then(response => {
        setPokemons(response.data.results)
      console.log(response)
      })
      .catch((err) => console.log(err))
      
    
    }
    return (
      <div className="App">
      
        <button onClick = {axiosPokemon}>Fetch Pokemno</button>

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
