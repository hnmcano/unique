import { useQuery } from "@tanstack/react-query";
import api from "../api/api";

const fetchProdutos = async () => {
    const { data } = await api.get("/produtos/react/catalago");
    return data;
};

export const useProdutos = () => {
    const {
        data: base = [],
        isLoading,
        isFetching,
        error,
        refetch
    } = useQuery({
        queryKey: ["produtos-catalogo"],
        queryFn: fetchProdutos,
        staleTime: 1000 * 60 * 5,   // 5 minutos cache
        cacheTime: 1000 * 60 * 30,  // 30 minutos em memória
        refetchOnWindowFocus: false
    });

    return {
        base,
        isLoading,
        isFetching,
        error,
        refetch
    };
};
