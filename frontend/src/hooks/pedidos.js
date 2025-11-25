import { useEffect, useState, useCallback  } from "react";
import api from "../api/api";


export const usePedidos = (id) => {
    const [solicitacao, setSolicitacao] = useState([]);
    const [ fecthLoading, fecthSetLoading ] = useState(false);
    const [ fecthError, fecthSetError ] = useState(null);


    const fetchSolicitacao = useCallback(async (dataToSend) => {

        fecthSetLoading(true);
        fecthSetError(null);

        try {
            const response = await api.post(`pedidos/react`, dataToSend);
            console.log('Resposta do servidor:', response.data);
            setSolicitacao(response.data);
            alert('Pedido enviado com sucesso!');
        } catch (error) {
            console.error('Erro ao enviar dados:', error);
            alert('Erro ao enviar pedido. Verifique o console.');
        }
    }, []);


    return {
        solicitacao, 
        setSolicitacao,
        fecthLoading,
        fecthError,
        fetchSolicitacao
    };

}