import { createContext, useContext, useState, useEffect } from "react";
import { useCarrinho } from "./CarrinhoContext";
import { useEstabelecimento } from "./EstabelecimentoContext";

const CheckoutContext = createContext();

export function CheckoutProvider({ children }) {
    const { produtos, totalCarrinho } = useCarrinho();
    const { estabelecimento } = useEstabelecimento();
    const [ formaPagamento, setFormaPagamento ] = useState(null);
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
        opcoes_pagamento: "",
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
            taxa_entrega: 0,
            distancia: 0,
            faixa_km: ""
        }
    });

    console.log(data);

    const totalQuantidade = produtos.reduce(
        (acc, p) => acc + p.quantidade, 0
    );

    const valor_total_com_taxa = totalCarrinho + data.entrega.taxa_entrega

    useEffect(() => {
        setData(prevState => ({
            ...prevState,
            itens: produtos.map(p => ({
                produto_id: p.produto_id,
                quantidade: p.quantidade,
                valor_unitario: p.preco_venda,
            })),
            valor_total: valor_total_com_taxa
        }));
    }, [produtos, totalCarrinho, totalQuantidade, data.entrega.taxa_entrega]);

    const SelecionarMetodo = (metodo) => {

        setOpcoesDisponiveis(prev =>
            prev === metodo ? null : metodo
        );

        setData(prevState => ({
            ...prevState,
            metodo_pagamento: metodo,
            opcoes_pagamento: metodo === `${estabelecimento.telefone}` ? "" : "",
        }))

    };

    const SelecionarBandeira = (tipo) => {
        setFormaPagamento(tipo);

        setData(prevState => ({
            ...prevState,
            opcoes_pagamento: tipo
        }));
    }

    
    return (
        <CheckoutContext.Provider value={{ data, setData, produtos, totalQuantidade, totalCarrinho, SelecionarMetodo, opcoesDisponiveis, formaPagamento, valor_total_com_taxa, SelecionarBandeira }} >
            {children}
        </CheckoutContext.Provider>
    )
}

export function useCheckout() {
    return useContext(CheckoutContext);
}