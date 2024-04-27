import React, { useEffect, useState } from 'react'
import axios from 'axios'
import {Link, useNavigate} from 'react-router-dom'
import { Author } from '../../../server/models/author.model'

const List = () => {
        const [authors, setAuthors] = useState([])
        const nav = useNavigate()
        useEffect(()=>{
            axios.get('http://localhost:8000/api/authors')
            .then(res=>setAuthors(res.data))
            .catch(err=> console.log(err));
        },[])
        const deleteObj=(id)=>{
          axios.delete(`http://localhost:8000/api/authors/${id}`)
          .then(res=>{ setAuthors(authors.filter(a=>a._id !== id))
          })
          .catch(err=>console.log(err));
      }
  return (
    <div>
      <h1>Favorite authors</h1>
        <Link className='btn btn-info' to={"/author/new"}>Add an author</Link>
        <table className='table'>
            <thead>
                <tr>
                    <th>Author</th>
                    <th>Actions Available</th>
                </tr>
            </thead>
            <tbody>
                {authors.map((Author)=>(
                    <tr key={Author._id}>
                        <td>{Author.name}</td>
                        <td>
                            <button className='btn btn-danger' onClick={()=>nav(`/author/edit/${Author._id}`)}>Edit</button>
                            <button className="btn btn-primary" onClick={()=>deleteObj(Author._id)}>Delete</button></td>
                    </tr>
                ))}
            </tbody>
        </table>

    </div>
  )
}

export default List