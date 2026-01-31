import { createContext, useContext, useState, useEffect } from "react";
import { useCarrinho } from "./CarrinhoContext";

const CheckoutContext = createContext();

export function CheckoutProvider({ children }) {
    const { produtos } = useCarrinho();
    const [ opcoesDisponiveis, setOpcoesDisponiveis ] = useState({});
    const [ data, setData] = useState({

        "itens": [
            {
                produto_id: 0,
                quantidade: 0,
                valor_unitario: 0,
            }
        ],

        metodo_pagamento: "",
        valor_total: 0,
        observacoes: "",

        "cliente": {
            nome: "",
            email: "",
            telefone: "",
        },

        "entrega": {
        cep: "",
        endereco: "",
        numero: "",
        bairro: "",
        cidade: "",
        estado: "",
        complemento: "",
        referencia: "",
        taxa_entrega: 7.0,
    }
    });

    const totalValor = produtos.reduce(
        (acc, p) => acc + p.valor_total, 0
    );
    const totalQuantidade = produtos.reduce(
        (acc, p) => acc + p.quantidade, 0
    );

    const entregaTaxa = 7.0;

    const valorTotal = totalValor + 7.0;

    useEffect(() => {
        setData(prevState => ({
            ...prevState,
            itens: produtos.map(p => ({
                produto_id: p.produto_id,
                quantidade: p.quantidade,
                valor_unitario: p.preco_venda

            })),
            valor_total: totalValor + 7.0,
            
        }));
    }, [produtos, totalValor, totalQuantidade]);

    const ToogleVisibility = (metodo) => {

        const indexString = String(metodo);

        console.log(indexString);

        setOpcoesDisponiveis((prevState) => ({
            ...prevState,
            [indexString]: !prevState[indexString],
        }));
    }

    return (
        <CheckoutContext.Provider value={{ data, setData, produtos, totalQuantidade, totalValor, entregaTaxa, valorTotal, ToogleVisibility, opcoesDisponiveis }} >
            {children}
        </CheckoutContext.Provider>
    )
}

export function useCheckout() {
    return useContext(CheckoutContext);
}