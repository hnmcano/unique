import { Navigate } from "react-router-dom";
import { useData } from "../Context/ContextData";

function isTokenExpired(token) {
    try {
        const payload = JSON.parse(atob(token.split(".")[1]));
        return payload.exp * 1000 < Date.now();
    } catch {
        return true; // token inválido
    }
}

export default function PrivateRoute({ children }) {
    const { token, setToken } = useData();

    if (!token || isTokenExpired(token)) {
        setToken(null); // limpa token expirado
        return <Navigate to="/" replace />;
    }

    return children;
}