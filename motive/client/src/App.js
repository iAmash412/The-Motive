import './index.css';
import React, { useState, useEffect } from 'react';
import * as Pages from './pages';
import { Routes, Route } from 'react-router-dom';
import { Deploy } from './components/Deploy';

function App() {
  const [state, setState] = useState({});

  useEffect(() => {
    fetch('/data')
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
      })
      .then((data) => setState(data))
      .then((error) => console.log(error));
  }, []);

  return (
    <div id="app" className="container">
      <main>
        <Routes>
          <Route path="/" element={<Pages.LandingPage />} />
          <Route path="/Login" element={<Pages.LoginPage />} />
          <Route path="/Register" element={<Pages.RegisterPage />} />
          <Route path="/User" element={<Pages.UserPage />} />
          <Route path="/connect" element={<Deploy prop={state} />} />
          <Route path="*" element={<Pages.NotFoundPage />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
