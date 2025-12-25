import { useState, useEffect } from "react";
import api from "../api/api";

export const useProdutos = () => {
    const [base, setBase] = useState([]);

    useEffect(() => {      
        api.get(`/produtos/react/catalago`)
            .then(response => {
                setBase(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return {base, setBase};
}