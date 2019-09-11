import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {"X-CSRFToken": "csrfToken"}
});

export default instance;