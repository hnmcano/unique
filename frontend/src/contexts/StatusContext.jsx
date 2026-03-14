import { createContext, useContext, useState, useEffect } from "react";

const StatusContext = createContext();

export function StatusProvider({ children }) {

    const [pedidos, setPedidos] = useState(() => {
        const salvo = localStorage.getItem("pedidos_status");
        return salvo ? JSON.parse(salvo) : {};
    });

    useEffect(() => {
        localStorage.setItem("pedidos_status", JSON.stringify(pedidos));
    }, [pedidos]);

    const atualizarPedido = (dados) => {
        console.log(dados);
        setPedidos(prev => ({
            ...prev,
            [dados.id_pedido]: {
                ...prev[dados.id_pedido],
                ...dados
            }
        }));
    };

    return (
        <StatusContext.Provider value={{ pedidos, atualizarPedido }}>
            {children}
        </StatusContext.Provider>
    );
}

export function useStatus() {
    return useContext(StatusContext);
}