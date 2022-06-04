import React, { useState, useEffect } from 'react';
import httpClient from '../httpClient';

const UserPage = () => {
  const [user, setUser] = useState({ id: '', email: '' });

  useEffect(() => {
    (async () => {
      try {
        const resp = await httpClient.get(
          'https://the-motive-one.herokuapp.com/@me'
        );
        setUser(resp.data);
      } catch (error) {
        console.log('Not Authenticated');
      }
    })();
  });

  return (
    <div>
      <h1>Welcome to Your Profile page</h1>
      {user != null ? (
        <div>
          <h1>Logged In</h1>
          <h3>Email: {user.email}</h3>
          <h3>Password: {user.password}</h3>
        </div>
      ) : (
        <div>
          <p>You are not logged in</p>
          <div>
            <a href="/login">
              <button>Login</button>
            </a>
            <a href="/register">
              <button>Register</button>
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserPage;
