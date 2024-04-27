import React from 'react'
import {useNavigate} from 'react-router-dom'
import {useState} from 'react'
import axios from 'axios'
const Create = () => {
  const nav = useNavigate()
  const [name , setName] = useState("")
  const submitHandler =(e)=>{
    e.preventDefault()
    axios.post('http://localhost:8000/api/authors/new' , {name})
    .then(res=>{
        console.log(res);
        nav('/')
    })
    .catch(err=>{
      const errorResponse = err.response.data.errors;
      const errArray = []
      for(const key of Object.keys(errorResponse)){
          errArray.push(errorResponse[key].message)
      }
      setErrors(errArray)
  })
}


  return (
    <div>
      <h1>Create Author</h1>
        <form onSubmit ={(e)=>submitHandler(e)}>
            {errors.map((err,i)=>(
                <p className='text-danger' key={i}>{err}</p>
            )
        )}
            <label className='label-control'>Name</label>
            <input input type = "text" className='form-control' value={name} onChange = {(e) => setName(e.target.value)} />
            <div>    
                <button className='btn btn-success'>Create</button>
                
            </div>
        </form><button className='btn btn-secondary' onClick={()=> nav('/')}>Cancel</button>
    </div>
    
  )
}

export default Create