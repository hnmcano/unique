import "../styles/Pedidos.css";
import "../styles/Carrinho.css"// Descomente se for usar
import { useCarrinho } from "../hooks/useCarrinho";
import { useEffect, useState } from "react";
import api from "../api/api";

import FormularioPedido from "../components/Pedido/FormularioPedido";
import ListProdutosPedido from "../components/Pedido/ListProdutosPedido";
import FormasPagPedido from "../components/Pedido/FormasPagPedido";
import EnviarPedido from "../components/Pedido/EnviarPedido";

function DataFinalizacao() {
    const { produtos, fetchCarrinho } = useCarrinho();
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
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


    const totalValor = produtos.reduce((acc, p) => acc + p.valor_total, 0);
    const totalQuantidade = produtos.reduce((acc, p) => acc + p.quantidade, 0);

    const openModal = () => setModalShoppingOpen(true)
    const closeModal = () => setModalShoppingOpen(false)

    useEffect(() => {
        if (closeModal){
            fetchCarrinho();
        }
    }, [modalShoppingOpen, fetchCarrinho]);

    const handleChangeClient = (event) => {
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            cliente: {
                ...prevState.cliente,
                [name]: value
            }

        }));
    };

    const handledChangeEntrega = (event) =>{
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            entrega: {
                ...prevState.entrega,
                [name]: value
            }
        }));
    }    

    const handledChangeInfos = (event) => {
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            [name]: value,
        }));

    }

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

    const handledSubmit = async (event) => {
        event.preventDefault();
        console.log(data);
        const response = await api.post("/pedidos/react", data);
        console.log(response.data);

    }

    const handleBlurCEP = async (event) => {
        const cep = event.target.value.replace(/[^0-9]/g, '');
        console.log(cep);
        if (cep.length === 8) {
            try {
                const res = await api.get(`https://viacep.com.br/ws/${cep}/json/`);
                const endereco = await res.data;
                setData(prevState => ({
                    ...prevState,
                    entrega: {
                        ...prevState.entrega,
                        cep: endereco.cep,
                        endereco: endereco.logradouro,
                        bairro: endereco.bairro,
                        cidade: endereco.localidade,
                        estado: endereco.uf,
                    }
                }));

            } catch (error) {
                console.log(error);
            }
        }
    }

    return (
        <div className="container__">
            <FormularioPedido  data={data} handleChangeClient={handleChangeClient} handledChangeEntrega={handledChangeEntrega} handleBlurCEP={handleBlurCEP} />
            <ListProdutosPedido produtos={produtos} totalQuantidade={totalQuantidade} totalValor={totalValor} />
            <FormasPagPedido data={data} handledChangeInfos={handledChangeInfos} openModal={openModal} closeModal={closeModal}/>
            <EnviarPedido data={data} handledSubmit={handledSubmit} openModal={openModal} modalShoppingOpen={modalShoppingOpen} handledChangeInfos={handledChangeInfos} />
        </div>
    );
}

export default DataFinalizacao;