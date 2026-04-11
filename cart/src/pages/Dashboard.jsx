import HeaderDash from "../components/headerDash";
import BodyDash from "../components/bodyDash";
import FooterDash from "../components/footerDash";
import { GetDados } from "../hooks/get";
import { useEffect } from "react";
import { useData } from "../Context/ContextData";

export default function Dashboard() {
    const {setData, token} = useData();
    
    useEffect(() => {
        async function fetchDados() {
        try {
            const response = await GetDados(token);
            setData(response.data); // ajuste conforme a estrutura da resposta
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
        }
        }

        if (token) fetchDados();
    }, [token]);

    return (
        <div className="h-screen">
            <HeaderDash />
            <main className="flex flex-col min-h-full">
                <BodyDash />
            </main>
            <FooterDash />
        </div>
    )
}