import HeaderDash from "../components/headerDash";
import BodyDash from "../components/bodyDash";
import FooterDash from "../components/footerDash";
import { GetDados, GetExecutavel } from "../hooks/get";
import { useEffect } from "react";
import { useData } from "../Context/ContextData";

export default function Dashboard() {
    const {setExecutavel, setData, token} = useData();

    useEffect(() => {
        async function fetchDados() {
            try {
                const response = await GetDados(token);
                setData(response.data); // ajuste conforme a estrutura da resposta
            } catch (error) {
                console.error("Erro ao buscar dados:", error);
            }
        }

        async function fetchExecutavel() {
            try {
                const response = await GetExecutavel(token);
                console.log("Executavel:", response.data);
                setExecutavel(response.data); // ajuste conforme a estrutura da resposta
            } catch (error) {
                console.error("Erro ao buscar dados:", error);
            }
        }

        if (token) fetchDados() && fetchExecutavel();
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