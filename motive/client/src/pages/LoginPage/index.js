import React, { useState } from 'react';
import httpClient from '../httpClient';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const logInUser = async () => {
    console.log(email, password);

    try {
      const resp = await httpClient.post(
        'https://the-motive-one.herokuapp.com/login',
        {
          email,
          password,
        }
      );
      console.log(resp.data);
      //   window.location.href = '/User';
    } catch (error) {
      if (error.response.status === 401) {
        alert('Invalid Credentials');
      }
    }
  };

  return (
    <div>
      <h1>Welcome to the login page</h1>
      <h2>Log into your account</h2>
      <form>
        <div>
          <label>Email</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            id=""
          ></input>
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            id=""
          ></input>
        </div>
        <button type="button" onClick={() => logInUser()}>
          Submit
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
