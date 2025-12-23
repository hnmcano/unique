import React, { useEffect, useState } from "react";
import api from "../api/api";


const useEstabelecimento = () => {
    const [base, setBase] = useState([]);

    useEffect(() => {
        api.get(`/estabelecimento/react/catalago`)
            .then(response => {
                setBase(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return {base, setBase};
}

export default useEstabelecimento;