import { createContext, useContext, useState, useEffect } from "react";

const CarrinhoContext = createContext();

const DUAS_HORAS_MS = 6 * 60 * 60 * 1000;

function carregarCarrinhoSalvo() {
    try {
        const salvo = localStorage.getItem("carrinho");
        if (!salvo) return [];

        const { produtos, timestamp } = JSON.parse(salvo);
        if (!Array.isArray(produtos)) return [];

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
    const [valorSelected, setValorSelected] = useState(null);
    const [produtos, setProdutos] = useState(() => carregarCarrinhoSalvo());

    useEffect(() => {
        localStorage.setItem("carrinho", JSON.stringify({
            produtos,
            timestamp: Date.now(),
        }));
    }, [produtos]);

    useEffect(() => {
        const intervalo = setInterval(() => {
            const salvo = localStorage.getItem("carrinho");
            if (!salvo) return;

            const { timestamp } = JSON.parse(salvo);
            if (Date.now() - timestamp > DUAS_HORAS_MS) {
                setProdutos([]);
                localStorage.removeItem("carrinho");
            }
        }, 60000);

        return () => clearInterval(intervalo);
    }, []);

    // 🔑 ID ÚNICO REAL (resolve tudo)
    const gerarIdItem = (p) => {
        const tamanho = p.tamanho && p.tamanho !== "" ? p.tamanho : "UNICO";
        return `${p.produto_id}-${tamanho}`;
    };

    const montarNome = (p) => {
        const nomeBase = p.nome || "Produto";
        return p.tamanho ? `${nomeBase}` : nomeBase;
    };

    function adicionarProduto(novoProduto) {
        const id_item = gerarIdItem(novoProduto);

        setProdutos(prev => {
            const existente = prev.find(p => p.id_item === id_item);

            if (existente) {
                const novaQuantidade = existente.quantidade + novoProduto.quantidade;

                return prev.map(p =>
                    p.id_item === id_item
                        ? {
                            ...p,
                            quantidade: novaQuantidade,
                            valor_total: novaQuantidade * p.preco_venda
                        }
                        : p
                );
            }

            return [
                ...prev,
                {
                    ...novoProduto,
                    id_item,
                    nome: montarNome(novoProduto),
                    quantidade: novoProduto.quantidade,
                    valor_total: novoProduto.quantidade * novoProduto.preco_venda
                }
            ];
        });
    }

    function removerProduto(id_item) {
        setProdutos(prev => prev.filter(p => p.id_item !== id_item));
    }

    function atualizarQuantidade(id_item, delta) {
        setProdutos(prev =>
            prev.map(p => {
                if (p.id_item !== id_item) return p;

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
            produtos,
            setProdutos,
            adicionarProduto,
            atualizarQuantidade,
            removerProduto,
            totalCarrinho,
            produtoModalOpen,
            setProdutoModalOpen,
            valorSelected,
            setValorSelected
        }}>
            {children}
        </CarrinhoContext.Provider>
    );
}

export function useCarrinho() {
    return useContext(CarrinhoContext);
}