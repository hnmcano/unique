import { createContext, useContext, useState, useEffect } from "react";
import { useCarrinho } from "./CarrinhoContext";

const CheckoutContext = createContext();

export function CheckoutProvider({ children }) {
    const { produtos } = useCarrinho();
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
        taxa_entrega: 0,
    }
    });

    const totalValor = produtos.reduce(
        (acc, p) => acc + p.valor_total, 0
    );
    const totalQuantidade = produtos.reduce(
        (acc, p) => acc + p.quantidade, 0
    );

    const entregaTaxa = 7.0;

    const valor_total = totalValor + entregaTaxa;

    useEffect(() => {
        setData(prevState => ({
            ...prevState,
            itens: produtos.map(p => ({
                produto_id: p.produto_id,
                quantidade: p.quantidade,
                valor_unitario: p.preco_venda
            })),
            valor_total: totalValor + entregaTaxa,
            
        }));
    }, [produtos, totalValor, totalQuantidade]);

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
        console.log("forma de pagamento: " + tipo);

        setData(prevState => ({
            ...prevState,
            metodo_pagamento: tipo,
        }));

        console.log(data);
    }

    return (
        <CheckoutContext.Provider value={{ data, setData, produtos, totalQuantidade, totalValor, entregaTaxa, valor_total, ToogleVisibility, opcoesDisponiveis, formaPagamento, handleSelect }} >
            {children}
        </CheckoutContext.Provider>
    )
}

export function useCheckout() {
    return useContext(CheckoutContext);
}