import React from 'react'
import {useParams} from 'react-router-dom'

const Color = () => {
    const {word,color1 , color2} = useParams();

    
    

  return (
    <div>
      
        <h1 style = {{backgroudColor:color1,color2}} >the word is : {word}</h1>

        
    </div>
  )
}

export default Color