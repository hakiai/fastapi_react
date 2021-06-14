import React from 'react'
import axios from 'axios'

export const HomePage: React.FC = () => {
  return (
    <>
      <div>Hello World!</div>
      {/* FIXME: 疎通確認用ボタン */}
      <button onClick={() => axios.post(`${process.env.REACT_APP_BASE_URL}/test`).then(data => console.log(data))}>test</button>
    </>
  )
}
