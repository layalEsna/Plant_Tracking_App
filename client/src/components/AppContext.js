
import React, { createContext, useState, useEffect} from 'react'

const AppContext = createContext()
export const AppProvider = ({ children }) => {
    const [user, setUser] = useState(null)
    const [plants, setPlants] = useState([])
    function setPlantsData(plantsData) {
        setPlants(plantsData)
    }


    useEffect(() => {
        
        fetch('/check_session')
            .then(res => {
                if (!res.ok) {
                throw new Error('Failed to fetch data.')
                }
                return res.json()
        })
            .then(data => {
                if(data && data.id){
                    setUser(data)
                } else {
                    setUser(null)
                }
                
        })
        .catch(e=> console.error(e))
    }, [])

   
    return (
        <AppContext.Provider value={{ user, setUser, plants, setPlants }}>
            {children}
        </AppContext.Provider>
    )
}

export default AppContext