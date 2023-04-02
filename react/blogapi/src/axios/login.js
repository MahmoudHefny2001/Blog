import axios from 'axios';

// const baseURL = 'https://hefnyspace.onrender.com/';

// const baseURL = 'https://kaxc3oyqa2.execute-api.us-west-2.amazonaws.com/';

const baseURL = 'https://hefny-blog.up.railway.app/'

const axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        accept: 'application/json',
    },
});

export default axiosInstance;