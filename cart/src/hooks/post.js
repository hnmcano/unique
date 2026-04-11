import api from "../api/api";

export async function PostLogin(formData) {
    const response = await api.post("/usuarios/login", formData);
    return response;
}

export async function PostRegister() {
    const response = await api.post("/register");
    console.log(response);
    return response;
}