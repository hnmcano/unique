import { useState, useEffect, useCallback } from "react";
import api from "../api/api";

export const useCarrinho = () => {
    const [produtos, setProdutos] = useState([]);
    const [quantidadeItems, setQuantidadeItems] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    // Função para buscar os dados do carrinho (Usada no useEffect e em refetch)
    const fetchCarrinho = useCallback(async (shouldFormat = true) => {
        setIsLoading(true);
        setError(null);
        try {
            const response = await api.get("/carrinho/carrinho");
            let dados = response.data.dataframe;
            let qtd = response.data.qtdprodutos;
            
            if (shouldFormat) {
                // Formata os dados para garantir que 'quantidade' exista
                dados = dados.map(item => ({
                    ...item,
                    quantidade: item.quantidade || 1, 
                }));
            }
            
            setProdutos(dados);
            setQuantidadeItems(qtd);
            return {dados,qtd}; // Retorna os dados para uso imediato, se necessário
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

    const removerProduto = async (product_id) => {
        try {
            let response = await api.delete(`/carrinho/delete/${product_id}`);
            let qtdprodutos = response.data.qtdprodutos

            console.log('Resposta do servidor:', qtdprodutos);

            setQuantidadeItems(qtdprodutos);

            return { qtdprodutos: qtdprodutos };
        } catch (error) {
            console.error('Erro ao excluir o produto:', error);
        }
    };

    return {
        produtos, 
        setProdutos, 
        isLoading, 
        error,
        fetchCarrinho, // Permite refazer a busca manualmente
        delCartShopping, 
        quantidadeItems,
        removerProduto
    };
};