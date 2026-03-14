import React, { useEffect } from 'react';
import { useEstabelecimento } from '../../contexts/EstabelecimentoContext';
import { useStatus } from "../../contexts/StatusContext";
import { GiConfirmed } from "react-icons/gi";
import { useParams } from "react-router-dom";
import dayjs from "dayjs";
import "../../styles/StatusPedido.css";

export default function AcompanhamentoPedido() {
    const { estabelecimento } = useEstabelecimento();
    const { id_pedido } = useParams();
    const { pedidos, atualizarPedido } = useStatus();

    const pedido = pedidos[id_pedido];

    const data_pedido = dayjs(pedido.data_criacao).format('DD/MM/YYYY');
    const hora_pedido = dayjs(pedido.data_criacao).format('hh:mm:ss');

    useEffect(() => {  
        if (!pedidos || pedidos.id_pedido !== id_pedido) {
            fetch(`https://api.uniqsystems.com.br/pedidos/${id_pedido}`)
            .then((response) => {response.json()
                .then((data) => {
                    atualizarPedido(data);
                })                
            })
        }

        const socket = new WebSocket(`wss://api.uniqsystems.com.br/ws/pedidos/${id_pedido}`);

        console.log(socket)

        socket.onmessage = (event) => {
            console.log(event);
            const data = JSON.parse(event.data);
            const { tipo, dados } = data;

            if (tipo === "pedido_status") {
                atualizarPedido(dados);
            }

        };
        return () => socket.close();

    }, [id_pedido]);

    if (!pedidos) {
        return <p>Carregando Pedido...</p>;
    }

    return (
        <>
            <div className="container-pedido">
                <GiConfirmed className='icone-status-pedido' />
                <div className='container-status-pedido'>
                    <p>{pedido.status}</p>
                </div>
                <div className='container-data-pedido'>
                    <label className='label-id_pedido'>ID: {pedido.id_pedido}</label>
                    <div className='label-nome-cliente'>
                        <span>Cliente:</span> 
                        <span>{pedido.cliente.nome}</span>
                    </div>
                    <div className='informacoes-data-hora'>
                        <div className='data-data_criacao'>
                            <span>Data Pedido:</span>
                            <label>{data_pedido}</label>
                        </div>
                        <div className='data-data_criacao'>
                            <span>Hora Pedido:</span>
                            <label>{hora_pedido}</label>
                        </div>
                    </div>
                    <div className='informacoes-prazo-entrega'>
                        <span>Prazo Entrega:</span>
                        <label>50 min à 70min</label>
                    </div>
                    <div className='informacoes-valor-total'>
                        <span>Valor Total:</span>
                        <label>{pedido.valor_total.toFixed(2)}</label>
                    </div>
                    <div className='informacoes-entrega-endereco'>
                        <span>Endereço de Entrega:</span>
                        <label>{pedido.endereco_entrega.endereco}, {pedido.endereco_entrega.numero}</label>
                    </div>
                </div>
                <div>
                    <div className='informacoes-contato'>
                        <span>Qualquer Duvida, entre em contato:</span>
                        <span onClick={() => window.open("https://wa.me/" + estabelecimento?.telefone)} className="contact-link">📞 {estabelecimento?.telefone}</span>
                    </div>
                </div>
            </div>
        </>
    );
}