import React, { useState } from 'react';



const PersonCard = (props) => {
    const {firstName,lastName,age,hairColor} = props;
        const [newAge , setnewAge] = useState(age)
    
    const handleBirthdayClick = () => {
        setnewAge(newAge + 1);

        
        };





    return (
        <div>
            <h2>
                {firstName} , {lastName}
            </h2>
            <p>Age : {newAge}</p>
            <p>hair Color : {hairColor}</p>
            <button onClick={ handleBirthdayClick }>Click Me</button>
        </div>
)

};



export default PersonCard;  
    