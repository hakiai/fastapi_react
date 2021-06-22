import React from 'react';
import { useState } from 'react';

import { readUserMe } from '../apicalls/auth'

export const HomePage: React.FC = () => {
  const [message, setMessage] = useState('Hello World!');

  return (
    <>
      <div>{message}</div>
      {/* FIXME: 疎通確認用ボタン */}
      <button
        onClick={() => {
          readUserMe().then((data) => {
            console.log(data)
          })
        }}
      >
        test
      </button>
    </>
  );
};
