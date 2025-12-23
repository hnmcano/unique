import React, { useEffect, useState } from "react";
import api from "../api/api";


const useEstabelecimento = () => {
    const [ BaseEstabelecimento, setBaseEstabelecimento] = useState([]);

    useEffect(() => {
        api.get(`/estabelecimento/react/catalago`)
            .then(response => {
                setBaseEstabelecimento(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return { BaseEstabelecimento, setBaseEstabelecimento };
}

export default useEstabelecimento;