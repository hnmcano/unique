import axios from "axios";
import { getSlugFromHost } from "../utils/tenant";

console.log("API URL:", import.meta.env.VITE_API_URL)

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

api.interceptors.request.use((config) => {
    const slug = getSlugFromHost();
    if (slug) {
        config.headers['x-tenant-slug'] = slug;
    }

    return config;
});

export default api;

