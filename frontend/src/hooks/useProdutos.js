import { useQuery } from "@tanstack/react-query";
import api from "../api/api";
import { getSlugFromHost } from "../utils/tenant";

const fetchProdutos = async () => {
    const { data } = await api.get("/produtos/react/catalogo");
    console.log(data);
    return data;
};

export const useProdutos = () => {
    const slug = getSlugFromHost();

    const {
        data: base = [],
        isLoading,
        isFetching,
        error,
        refetch
    } = useQuery({
        queryKey: ["produtos-catalogo", slug],
        queryFn: fetchProdutos,
        enabled: !!slug,              // Evita chamadas sem slug
        retry: false,                 // Não tenta novamente em 404
        staleTime: 1000 * 60 * 5,
        cacheTime: 1000 * 60 * 30,
        refetchOnWindowFocus: false,
        onError: (err) => {
            if (err.response && err.response.status === 404) {
                console.error("Erro 404: Produto não encontrado.");
                // Interrompe ou trata como necessário, por exemplo, não refetchar.
            }
        },
    });

    return {
        base,
        isLoading,
        isFetching,
        error,
        refetch
    };
};