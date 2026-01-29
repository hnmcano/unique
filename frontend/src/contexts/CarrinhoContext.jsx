import { createContext, useContext, useState, useEffect, use } from "react";

const CarrinhoContext = createContext();

export function CarrinhoProvider({ children }) {

    const [produtos, setProdutos] = useState(() => {
        const salvo = localStorage.getItem("carrinho");
        return salvo ? JSON.parse(salvo) : [];
    });

    useEffect(() => {
        localStorage.setItem("carrinho", JSON.stringify(produtos));
    }, [produtos]);

    console.log("CarrinhoContext - produtos:", produtos);

    function adicionarProduto(novoProduto) {

        setProdutos(prevProdutos => {
            const produtoExistente = prevProdutos.find(p => p.produto_id === novoProduto.produto_id);

            if (produtoExistente) {
                return prevProdutos.map(p =>
                    p.produto_id === novoProduto.produto_id
                        ? 
                        { 
                        ...p, 
                            quantidade: p.quantidade + novoProduto.quantidade,
                            valor_total: (p.quantidade + 1) * p.preco_venda
                        }
                    : p
                );
            } else {
                return [
                ...prevProdutos, 
                    { 
                    ...novoProduto, 
                        quantidade: novoProduto.quantidade,
                        valor_total: novoProduto.preco_venda
                    }
                ];
            }

        });
    }

    function removerProduto(produtoId) {
        setProdutos(prevProdutos => prevProdutos.filter(p => p.produto_id !== produtoId));
    }

    function atualizarQuantidade(produtoId, delta) {
        setProdutos(prev =>
            prev.map(p => { 
                if (p.produto_id !== produtoId) return p;

                const novaQuantidade = Math.max(1, p.quantidade + delta);

                return {
                    ...p,
                    quantidade: novaQuantidade,
                    valor_total: novaQuantidade * p.preco_venda
                };
            })
        );
    }

    const totalCarrinho = produtos.reduce((acc, p) => acc + p.valor_total, 0);

    return (
        <CarrinhoContext.Provider value={{ produtos, setProdutos, adicionarProduto, atualizarQuantidade, removerProduto, totalCarrinho }} >
            {children}
        </CarrinhoContext.Provider>
    );
}

export function useCarrinho() {
    return useContext(CarrinhoContext);
}