import React from 'react';
import { useState } from 'react';

import { readUserMe } from '../apicalls/auth'

export const HomePage: React.FC = () => {
  const [message, setMessage] = useState('Hello World!');

  return (
    <>
      <div>{message}</div>
      {/* FIXME: 疎通確認用ボタン(必要なければ削除) */}
      <button
        onClick={() => {
          readUserMe().then((data: any) => {
            console.log(data.data)
          })
        }}
      >
        test
      </button>
    </>
  );
};
