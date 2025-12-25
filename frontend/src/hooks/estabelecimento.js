import React, { useEffect, useState } from "react";
import api from "../api/api";

export function useEstabelecimento() {
    const [ BaseEstabelecimento, setBaseEstabelecimento] = useState(null);

    useEffect(() => {
        api.get(`/estabelecimento/react/catalago`)
            .then(response => {
                setBaseEstabelecimento(response.data[0]);
                console.log(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return [ BaseEstabelecimento, setBaseEstabelecimento];
}


