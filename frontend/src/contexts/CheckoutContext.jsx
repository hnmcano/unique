import { createContext, useContext, useState, useEffect } from "react";
import { useCarrinho } from "./CarrinhoContext";

const CheckoutContext = createContext();

export function CheckoutProvider({ children }) {
    const { produtos, totalCarrinho } = useCarrinho();
    const [ formaPagamento, setFormaPagamento ] = useState(null);
    const [ bandeiraCartao, setBandeiraCartao ] = useState(null);
    const [ opcoesDisponiveis, setOpcoesDisponiveis ] = useState(null)


    const [ data, setData] = useState({

        "itens": [
            {
                produto_id: 0,
                quantidade: 0,
                valor_unitario: 0,
            }
        ],

        metodo_pagamento: "",
        // bandeiraCartao: "",
        valor_total: 0,
        observacoes: "",

        "cliente": {
            nome: "",
            telefone: "",
            email: "",
            cpf: "",
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


    const totalQuantidade = produtos.reduce(
        (acc, p) => acc + p.quantidade, 0
    );

    const entregaTaxa = 7.0;

    const valor_total = totalCarrinho + entregaTaxa

    useEffect(() => {
        setData(prevState => ({
            ...prevState,
            itens: produtos.map(p => ({
                produto_id: p.produto_id,
                quantidade: p.quantidade,
                valor_unitario: p.preco_venda,
            })),
            valor_total: totalCarrinho  + entregaTaxa
        }));
    }, [produtos, totalCarrinho, totalQuantidade]);

    const ToogleVisibility = (metodo) => {
        setOpcoesDisponiveis(prev =>
            prev === metodo ? null : metodo
        );

        setData(prevState => ({
            ...prevState,
            metodo_pagamento: metodo,
        }));
    };

    const handleSelect = (tipo) => {
        setFormaPagamento(tipo);

        setData(prevState => ({
            ...prevState,
            metodo_pagamento: tipo,
        }));
    }

    
    return (
        <CheckoutContext.Provider value={{ data, setData, produtos, totalQuantidade, totalCarrinho, entregaTaxa, ToogleVisibility, opcoesDisponiveis, formaPagamento, valor_total, handleSelect }} >
            {children}
        </CheckoutContext.Provider>
    )
}

export function useCheckout() {
    return useContext(CheckoutContext);
}