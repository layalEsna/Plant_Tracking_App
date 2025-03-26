import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes, useLocation } from "react-router-dom";
import { AppProvider } from "./AppContext";
import Signup from "./Signup";
import Login from "./Login";
import LandingPage from "./LandingPage";

function App() {
  return (
    <AppProvider>
      <Router>
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/users/:user_id" element={<LandingPage/>} />
        </Routes>
      </Router>
    </AppProvider>
  )


}

export default App;
