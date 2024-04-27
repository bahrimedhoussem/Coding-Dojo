import React from 'react'
import {useParams} from 'react-router-dom'

const NumberId = () => {
    const {id} = useParams();
  return (
    <div>
        <h1>the number is : {id} </h1>
    </div>
  )
}

export default NumberId