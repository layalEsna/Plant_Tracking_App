
import React, { createContext, useState } from 'react'

const AppContext = createContext()
export const AppProvider = ({ children }) => {
    const [user, setUser] = useState(null)
    const [plants, setPlants] = useState([])
    function setPlantsData(plantsData) {
        setPlants(plantsData)
    }
    return (
        <AppContext.Provider value={{ user, setUser, plants, setPlants }}>
            {children}
        </AppContext.Provider>
    )
}

export default AppContext