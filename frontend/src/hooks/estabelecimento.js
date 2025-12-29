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


export function statusEstabelecimento() {
    const [ status, setStatus ] = useState("");

    useEffect(() => {
        api.get(`/caixa/valid_box`)
            .then(response => {
                if (response.data.status === 200) {
                    setStatus("ABERTO");
                } else {
                    setStatus("FECHADO");
                }
            })
            .catch(error => {
                console.error('Erro ao receber os dados do status:', error);
            });
    }, []);
    
    return status;
}
