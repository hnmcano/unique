import axios from "axios";

const urlapi = "http://localhost:8000";
// const urlapi = "https://api.uniqsystems.com.br";

const api = axios.create({
    baseURL: urlapi,
});

export default api;
