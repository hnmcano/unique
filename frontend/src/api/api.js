import axios from "axios";

const api = axios.create({
    baseURL: 'https://api.uniqsystems.com.br',
});

export default api;

