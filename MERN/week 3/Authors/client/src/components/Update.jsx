import React from 'react'
import {useNavigate} from 'react-router-dom'
import {useState} from 'react'
import {useEffect} from 'react'
import axios from 'axios'
import {useParams} from 'react-router-dom'

const update = () => {
  const nav = useNavigate()
    const [name , setName] = useState("");
    const [errors , setErrors] = useState([]);
    const {id}= useParams()
    useEffect(()=>{
      axios.get("http://localhost:8000/api/authors/" + id)
      .then(res=>{
          setName(res.data.name)
      });
    },[id])
    const submitHandler =(e) =>{
      e.preventDefault()
      axios.put("http://localhost:8000/api/authors/" + id+"/update",{name})
      .then(res=>{
          nav("/")
      }).catch(
          err=>
          {const errorResponse = err.response.data.errors;
          const errArray = []
          for(const key of Object.keys(errorResponse)){
              errArray.push(errorResponse[key].message)
          }
          setErrors(errArray)});
  }
  return (
    <div>
      <div className='container'>
        <h1>Edit author</h1>
        <form onSubmit ={submitHandler}>
            {errors.map((err,i)=>(
                <p className='text-danger' key={i}>{err}</p>
            )
        )}
        <label className='label-control'>Name</label>
            <input input type = "text" className='form-control' value={name} onChange = {(e) => setName(e.target.value)} />
            <div className='d-flex justify-content-between'>
                <button className='btn btn-success'>Edit</button>
                <button className='btn btn-secondary' onClick={()=> nav('/')}>Cancel</button>
            </div>
        </form>
    </div>

    </div>
  )
}

export default update