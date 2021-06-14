import React from 'react';
import { useState } from 'react';
import axios from 'axios';

export const HomePage: React.FC = () => {
  const [message, setMessage] = useState('Hello World!')

  return (
    <>
      <div>{message}</div>
      {/* FIXME: 疎通確認用ボタン */}
      <button
        onClick={() =>
          axios
            .post(`${process.env.REACT_APP_BASE_URL}/test`)
            .then((data) => setMessage(data.data.message))
        }
      >
        test
      </button>
    </>
  );
};
