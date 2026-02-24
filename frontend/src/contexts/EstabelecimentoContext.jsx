import { useEffect, useState, createContext, useContext } from "react";
import api from "../api/api";

const EstabelecimentoContext = createContext();

export function EstabelecimentoProvider({ children }) {
    const [estabelecimento, setEstabelecimento] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        async function carregar() {
            try {
                const response = await api.get("/estabelecimento/dados_estabelecimento");
                setEstabelecimento(response.data);
                document.title = response.data.nome;
                console.log(response.data);
            } catch (error) {
                console.log(error);
            } finally {
                setIsLoading(false);
            }
            
        }
        carregar();
    }, []);
    
    return (
        <EstabelecimentoContext.Provider value={{ estabelecimento, isLoading }}>
            {children}
        </EstabelecimentoContext.Provider>
    );
}

export function useEstabelecimento() {
    return useContext(EstabelecimentoContext);
}