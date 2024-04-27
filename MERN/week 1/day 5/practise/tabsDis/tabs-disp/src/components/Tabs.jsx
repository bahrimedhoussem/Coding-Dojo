import React , {useState} from 'react'

const Tabs = () => {
    const tab = ["tab1" , "tab2" , "tab3"];
    const [msg,setMsg] = useState('')
    const clickhandler = (e ,y) => {
        e.preventDefault();
        setMsg(y + "content is showing here" );

    }
    return ( 
    <fieldset>
        <div>
        { tab.map((value,i)=>{
        return <button   key={i} onClick={(e)=> clickhandler(e,value,i)}>{value}</button>
    })
    }
    <p>{msg}</p>

        </div>
    </fieldset>
)
}

export default Tabs
