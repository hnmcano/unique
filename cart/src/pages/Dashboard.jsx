import HeaderDash from "../components/headerDash";
import BodyDash from "../components/bodyDash";
import FooterDash from "../components/footerDash";
import { GetDados, GetExecutavel } from "../hooks/get";
import { useEffect } from "react";
import { useData } from "../Context/ContextData";

export default function Dashboard() {
    const { setExecutavel, setData, token, setIsLoading, setError } = useData();

    useEffect(() => {
        if (!token) return;

        async function fetchTudo() {
                // 1. busca dados gerais primeiro
                try {
                    setIsLoading(true);
                    const response = await GetDados(token);
                    setData(response.data);
                } catch (error) {
                    setError(error);
                    console.error("Erro ao buscar dados:", error);
                } finally {
                    setIsLoading(false); // ← dashboard renderiza aqui
            }

            // 2. busca executável em segundo plano (sem bloquear o dashboard)
            fetchExecutavel();
        }

        async function fetchExecutavel() {
            try {
                setExecutavel({ loading: true, url: null }); // ← sinaliza carregando
                const response = await GetExecutavel(token);
                const blob = new Blob([response.data], { type: 'application/octet-stream' });
                const url = URL.createObjectURL(blob);
                setExecutavel({ loading: false, url });
            } catch (error) {
                setExecutavel({ loading: false, url: null });
                console.error("Erro ao buscar executável:", error);
            }
        }

        
        fetchTudo(); // ← chamada que faltava
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