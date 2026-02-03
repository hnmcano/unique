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
                produtoId: 0,
                quantidade: 0,
                valorUnitario: 0,
            }
        ],

        metodoPagamento: "",
        // bandeiraCartao: "",
        valorTotal: 0,
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
        taxaEntrega: 7.0,
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
                produtoId: p.produto_id,
                quantidade: p.quantidade,
                valorUnitario: p.preco_venda

            })),
            valorTotal: totalValor + 7.0,
            
        }));
    }, [produtos, totalValor, totalQuantidade]);

    const ToogleVisibility = (metodo) => {
        setOpcoesDisponiveis(prev =>
            prev === metodo ? null : metodo
        );

        setData(prevState => ({
            ...prevState,
            metodoPagamento: metodo,
        }));
    };

    const handleSelect = (tipo) => {
        setFormaPagamento(tipo);
        console.log("forma de pagamento: " + tipo);

        setData(prevState => ({
            ...prevState,
            metodoPagamento: tipo,
        }));

        console.log(data);
    }

    return (
        <CheckoutContext.Provider value={{ data, setData, produtos, totalQuantidade, totalValor, entregaTaxa, valorTotal, ToogleVisibility, opcoesDisponiveis, formaPagamento, handleSelect }} >
            {children}
        </CheckoutContext.Provider>
    )
}

export function useCheckout() {
    return useContext(CheckoutContext);
}