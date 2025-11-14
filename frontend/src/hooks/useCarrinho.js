import { useState, useEffect, useCallback } from "react";
import api from "../api/api";

export const useCarrinho = () => {
    const [produtos, setProdutos] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    // Função para buscar os dados do carrinho (Usada no useEffect e em refetch)
    const fetchCarrinho = useCallback(async (shouldFormat = true) => {
        setIsLoading(true);
        setError(null);
        try {
            const response = await api.get("/carrinho/carrinho");
            let dados = response.data;
            
            if (shouldFormat) {
                // Formata os dados para garantir que 'quantidade' exista
                dados = dados.map(item => ({
                    ...item,
                    quantidade: item.quantidade || 1, 
                }));
            }
            
            setProdutos(dados);
            return dados; // Retorna os dados para uso imediato, se necessário
        } catch (err) {
            console.error('Erro ao buscar dados do carrinho:', err);
            setError(err);
            return [];
        } finally {
            setIsLoading(false);
        }
    }, []);

    // 1. Efeito para carregar o carrinho na montagem
    useEffect(() => {
        fetchCarrinho();
    }, [fetchCarrinho]);


    // 2. FUNÇÃO DE AÇÃO: Deleta todos os itens do carrinho (usada no onClick)
    const delCartShopping = async () => {
        try {
            // Ação: Chama a API DELETE
            await api.delete("/carrinho/delete/all");
            
            // Sucesso: Limpa o estado local
            setProdutos([]); 
            
            return true;
        } catch (error) {
            console.error('Erro ao excluir todos os itens do carrinho:', error);
            // Opcional: Notificar o usuário do erro
            return false;
        }
    };
    
    // Você pode adicionar outras funções como update e delete de item individual aqui...

    return {
        produtos, 
        setProdutos, 
        isLoading, 
        error,
        fetchCarrinho, // Permite refazer a busca manualmente
        delCartShopping // A função de ação para o botão
    };
};

// ❌ O hook useProdutosCartShopping NÃO é mais necessário, 
// pois fetchCarrinho pode ser usado no useCarrinho para buscar os dados.

// ❌ O hook delCartShopping FOI MOVIMENTADO para DENTRO do useCarrinho, 
// transformando-o em uma função de ação, e não em um hook que executa na montagem.