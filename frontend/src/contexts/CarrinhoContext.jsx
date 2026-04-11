import { createContext, useContext, useState, useEffect } from "react";

const CarrinhoContext = createContext();

const DUAS_HORAS_MS = 6 * 60 * 60 * 1000;

function carregarCarrinhoSalvo() {
    try {
        const salvo = localStorage.getItem("carrinho");
        if (!salvo) return [];

        const { produtos, timestamp } = JSON.parse(salvo);
        const expirado = Date.now() - timestamp > DUAS_HORAS_MS;

        if (expirado) {
            localStorage.removeItem("carrinho");
            return [];
        }

        return produtos;
    } catch {
        localStorage.removeItem("carrinho");
        return [];
    }
}

export function CarrinhoProvider({ children }) {
    const [produtoModalOpen, setProdutoModalOpen] = useState(false);
    const [valorSelected, setValorSelected] = useState([]);
    const [produtos, setProdutos] = useState(carregarCarrinhoSalvo);

    // ✅ salva com timestamp sempre que o carrinho mudar
    useEffect(() => {
        localStorage.setItem("carrinho", JSON.stringify({
            produtos,
            timestamp: Date.now(),
        }));
    }, [produtos]);

    // ✅ verifica expiração a cada minuto enquanto a aba está aberta
    useEffect(() => {
        const intervalo = setInterval(() => {
            const salvo = localStorage.getItem("carrinho");
            if (!salvo) return;

            const { timestamp } = JSON.parse(salvo);
            if (Date.now() - timestamp > DUAS_HORAS_MS) {
                setProdutos([]);
                localStorage.removeItem("carrinho");
            }
        }, 60 * 1000);

        return () => clearInterval(intervalo);
    }, []);

    function adicionarProduto(novoProduto) {
        setProdutos(prevProdutos => {
            const produtoExistente = prevProdutos.find(p => p.produto_id === novoProduto.produto_id);

            if (produtoExistente) {
                return prevProdutos.map(p =>
                    p.produto_id === novoProduto.produto_id
                        ? {
                            ...p,
                            quantidade: p.quantidade + novoProduto.quantidade,
                            valor_total: (p.quantidade + novoProduto.quantidade) * p.preco_venda
                        }
                        : p
                );
            } else {
                return [
                    ...prevProdutos,
                    {
                        ...novoProduto,
                        quantidade: novoProduto.quantidade,
                        valor_total: novoProduto.quantidade * novoProduto.preco_venda
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
        <CarrinhoContext.Provider value={{
            produtos, setProdutos,
            adicionarProduto, atualizarQuantidade, removerProduto,
            totalCarrinho,
            produtoModalOpen, setProdutoModalOpen,
            valorSelected, setValorSelected
        }}>
            {children}
        </CarrinhoContext.Provider>
    );
}

export function useCarrinho() {
    return useContext(CarrinhoContext);
}