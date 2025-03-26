import { useContext, useEffect } from "react"
import AppContext from "./AppContext"
const LandingPage = () => {

    const { user, setUser } = useContext(AppContext)
    
     
    if (!user) {
        return <div>Loading ...</div>
    }
    return (
        <div>
           <h4>Welcome: {user.username}</h4>

        </div>
    )
}

export default LandingPage


