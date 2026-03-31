// importando as funções de estado, referencia e efeitos do React
import { useRef, useEffect, useState} from "react";

// importando função de Draggable para referenciar no DOM e permitir arrastar o modal
import Draggable from "react-draggable";
import { useHorarios } from "../contexts/HorariosContext";
import { useEstabelecimento } from "../contexts/EstabelecimentoContext";
import "../styles/Horarios.css";

// Função principal do modal carrinho, recebendo o estado de abertura e fechamento do modal
function Horarios(){
    // definindo estado de total de produtos no carrinho como 0
    const { openCard, setOpenCard} = useHorarios();
    const { estabelecimento } = useEstabelecimento();

    const diasSemana = [
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
        "Domingo"
    ];
    const dia_atual = new Date().getDay(); // 0 (Domingo) a 6 (Sábado)

    const style = estabelecimento?.cor_layout !== null
        ? { color: estabelecimento?.cor_layout, marginTop: 0 }
        : {};

    const classText = estabelecimento?.cor_layout === null ? "horarios-semanais" : "";

    // importando hooks (caminho: src/hooks/useCarrinho ) de carrinho que contem as funções para manipular o carrinho, como produtos, 
    // deletar todos os produtos, quantidade de produtos e remover produto.
    // definindo referencia para o modal como null
    const nodeRef = useRef(null);

    // Se o modal não estiver aberto, retorna null
    if (!openCard) return null;

    return (
    // Modal de carrinho
    <div className=" modal-overlay"             
            onClick={(e) => {
                e.stopPropagation();
                setOpenCard(false);
            }}>
        {/* O Modal pode ser arrastado devido a biblioteca Draggable com o nodeRef */}
        <Draggable nodeRef={nodeRef} handle=".modal-header-handle" bounds="parent">
            {/* Com o nodeRef estamos referenciando o modal, permitindo arrastar o modal, 
            onclick={(e) => e.stopPropagation()} impede que o modal seja fechado ao clicar no conteúdo */}
            <div ref={nodeRef} className="modal-horarios" onClick={(e) => e.stopPropagation()}>

                {/* O conteúdo que for passado (ex: seu formulário) */}
                <div className="modal-body">
                    <div className="modal-title">
                        <h1>Horários</h1>
                    </div>
                    {estabelecimento.horarios.map((horario, index) => (
                        <div className={diasSemana[horario.dia_semana] === diasSemana[dia_atual === 0 ? 6 : dia_atual - 1] ? "dia-atual" : "horarios-semanais"} key={index}>
                            <span>
                                {diasSemana[horario.dia_semana]}
                            </span>
                            <span>{horario.hora_abertura.slice(0, 5)} - {horario.hora_fechamento.slice(0, 5)}</span>
                        </div>
                    ))}
                </div>          
            </div>
        </Draggable>
    </div>
  );
}

{/* Exportando a função ModalShopping como padrão. */}
export default Horarios;