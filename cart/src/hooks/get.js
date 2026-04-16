import api from "../api/api";

export async function GetDados(token) {
    const response = await api.get("/estabelecimento/dados-gerais", {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });
    return response;
}


export async function GetExecutavel(token) {
    console.log(token);
    const response = await api.get("/update/", {
        headers: {
            Authorization: `Bearer ${token}`,
        },
        responseType: 'blob',
        // ← Remova o timeout também
    });
    return response;
}