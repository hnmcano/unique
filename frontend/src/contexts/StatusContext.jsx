import { createContext, useContext, useState, useEffect } from "react";

const StatusContext = createContext();

export function StatusProvider({ children }) {

    const [dataStatus, setDataStatus] = useState(() => {
        const salvo = localStorage.getItem("status");
        return salvo ? JSON.parse(salvo) : [];
    });

    useEffect(() => {
        localStorage.setItem("status", JSON.stringify(dataStatus));
    }, [dataStatus]);

    return (
        <StatusContext.Provider value={{ dataStatus, setDataStatus }}>
            {children}
        </StatusContext.Provider>
    );
    
}

export function useStatus() {
    return useContext(StatusContext);
}