import React , {Component} from 'react';



function PersonCard() {
    return (

        <div className= "person-card">

            <h1>{props.firstName}</h1>
            <h3><p>Age: {props.age}</p> </h3>
            <h3>Hair Color : {props.hairColor}</h3>

        </div>


    );


}