import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import { AppProvider } from "./AppContext";
import Signup from "./Signup";

function App() {
  return (
    <AppProvider>
      <Router>
        <Routes>
          <Route path='/signup' element={<Signup/>} />
        </Routes>
      </Router>
    </AppProvider>
  )


}

export default App;
