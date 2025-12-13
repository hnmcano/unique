import api from "../api/api";    
import axios from "axios";
import { useState, useEffect } from "react";    
import { GiReturnArrow } from "react-icons/gi";
    
export const useProdutos = () => {
    const [base, setBase] = useState([]);

    useEffect(() => {      
        axios.get("http://127.0.0.1:8000/produtos/react/catalago")
            .then(response => {
                setBase(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return {base, setBase};
}