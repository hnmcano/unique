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
        enabled: !!slug,              // 🔥 evita chamadas inválidas
        retry: false,                 // 🔥 evita spam em 404
        staleTime: 1000 * 60 * 5,
        cacheTime: 1000 * 60 * 30,
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