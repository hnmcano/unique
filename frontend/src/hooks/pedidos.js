import { useEffect, useState, useCallback  } from "react";
import api from "../api/api";


export const usePedidos = () => {
    const [solicitacao, setSolicitacao] = useState([]);
    const [ fecthLoading, fecthSetLoading ] = useState(false);
    const [ fecthError, fecthSetError ] = useState(null);


    const fetchSolicitacao = useCallback(async (dataToSend) => {

        fecthSetLoading(true);
        fecthSetError(null);

        try {
            const response = await api.post(`pedidos/react`, dataToSend);
            setSolicitacao(response.data);
        } catch (error) {

            fecthError(error);

            return {
                success: false,
                error: error.response?.data
            }
        } finally {
            fecthSetLoading(false);
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