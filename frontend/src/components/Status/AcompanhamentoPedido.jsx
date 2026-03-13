import React, { useEffect } from 'react';
import { useStatus } from "../../contexts/StatusContext";
import { GiConfirmed } from "react-icons/gi";
import { useParams } from "react-router-dom";
import dayjs from "dayjs";
import "../../styles/StatusPedido.css";

export default function AcompanhamentoPedido() {
    const { id_pedido } = useParams();
    const { dataStatus, setDataStatus } = useStatus();
    const data_pedido = dayjs(dataStatus.data_criacao).format('DD/MM/YYYY');
    const hora_pedido = dayjs(dataStatus.data_criacao).format('hh:mm:ss');


    useEffect(() => {  
        if (!dataStatus || dataStatus.id_pedido !== id_pedido) {
            fetch(`https://api.uniqsystems.com.br/pedidos/${id_pedido}`)
            .then((response) => {response.json()
                .then((data) => {
                    setDataStatus(data);
                })                
            })
        }

        const socket = new WebSocket(`wss://api.uniqsystems.com.br/ws/pedidos/${id_pedido}`);

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setDataStatus(prev => 
                ({ 
                    ...prev, 
                    ...data 
                }));
        };
        return () => socket.close();

    }, [id_pedido]);

    if (!dataStatus) {
        return <p>Carregando Pedido...</p>;
    }

    return (
        <>
            <div className="container-pedido">
                <GiConfirmed className='icone-status-pedido' />
                <div className='container-status-pedido'>
                    <p>{dataStatus.status}</p>
                </div>
                <div className='container-data-pedido'>
                    <label className='label-id_pedido'>ID: {dataStatus.id_pedido}</label>
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
                        <label>{dataStatus.valor_total.toFixed(2)}</label>
                    </div>
                    <div className='informacoes-entrega-endereco'>
                        <span>Endereço de Entrega:</span>
                        <label>{dataStatus.endereco_entrega.endereco}, {dataStatus.endereco_entrega.numero}</label>
                    </div>
                </div>
            </div>
        </>
    );
}