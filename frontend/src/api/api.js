import axios from "axios";

//const urlapi = "http://127.0.0.1:8000";
const urlapi = "https://api.uniqsystems.com.br";

const api = axios.create({
    baseURL: urlapi,
});

export default api;
