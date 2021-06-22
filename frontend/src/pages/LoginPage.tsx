import React from 'react';
import { useState } from 'react';
import { useHistory } from 'react-router-dom'

import { login } from '../apicalls/auth';

export const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('')

  const history = useHistory()

  const pushLoginBtn = (email: string, password: string) => {
    login(email, password).then((data) => {
      console.log(data)
      console.log(data.status)
      if (data.data.status_code === 400) {
        return setErrorMessage(data.data.detail)
      }
      history.push('/')
    });
  };

  return (
    <>
      <div>Login</div>
      <div>
        <div>
          Email:
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          Password:
          <input
            type="text"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
      </div>
      <div>
        <button onClick={() => pushLoginBtn(email, password)}>Login</button>
      </div>
      <div style={{ color: 'red' }}>
        { errorMessage }
      </div>
    </>
  );
};
