import axios from '../plugins/axios';

export const login = (email: string, password: string) => {
  return axios
    .post(
      '/login',
      {
        email,
        password,
      },
      {
        headers: {
          withCredentials: true,
        },
      }
    )
    .then((data) => {
      return data;
    })
    .catch((err) => {
      return err.response;
    });
};

export const readUserMe = () => {
  return axios
    .get('/users/me', {
        withCredentials: true,
    })
    .then((data) => {
      return data;
    })
    .catch((err) => {
      return err.response;
    });
};
