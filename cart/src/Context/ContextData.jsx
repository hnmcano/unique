import { createContext, useContext, useEffect, useState } from "react";

const contextData = createContext();

export function ContextProvider({children}) {
    const [data, setData] = useState({});
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);
    const [token, setTokenState] = useState(() => localStorage.getItem("token") ?? null);
    const [executavel, setExecutavel] = useState(false);

    function setToken(value) {
        if (value) {
            localStorage.setItem("token", value);
        } else {
            localStorage.removeItem("token");
        }
        setTokenState(value);
    }

    return (
        <contextData.Provider value={{data, setData, token, setToken, isLoading, setIsLoading, error, setError, executavel, setExecutavel}}>
            {children}
        </contextData.Provider>
    )
}   

export function useData() {
    return useContext(contextData);
}