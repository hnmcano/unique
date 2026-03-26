// importando as funções de estado, referencia e efeitos do React
import { useRef, useEffect} from "react";

// importando função de Draggable para referenciar no DOM e permitir arrastar o modal
import Draggable from "react-draggable";
import { useHorarios } from "../contexts/HorariosContext";

// Função principal do modal carrinho, recebendo o estado de abertura e fechamento do modal
function Horarios(){
    // definindo estado de total de produtos no carrinho como 0
    const { openCard, setOpenCard} = useHorarios();
    
    // importando hooks (caminho: src/hooks/useCarrinho ) de carrinho que contem as funções para manipular o carrinho, como produtos, 
    // deletar todos os produtos, quantidade de produtos e remover produto.
    // definindo referencia para o modal como null
    const nodeRef = useRef(null);

    // Se o modal não estiver aberto, retorna null
    if (!openCard) return null;

    return (
    // Modal de carrinho
    <div className="modal-overlay"             
            onClick={(e) => {
                e.stopPropagation();
                setOpenCard(false);
            }}>
        {/* O Modal pode ser arrastado devido a biblioteca Draggable com o nodeRef */}
        <Draggable nodeRef={nodeRef} handle=".modal-header-handle" bounds="parent">
            {/* Com o nodeRef estamos referenciando o modal, permitindo arrastar o modal, 
            onclick={(e) => e.stopPropagation()} impede que o modal seja fechado ao clicar no conteúdo */}
            <div ref={nodeRef} className="modal-content" onClick={(e) => e.stopPropagation()}>
                {/* O cabeçalho do modal */}
                <div className="modal-header-handle">
            <button
            onTouchStart={(e) => {
                e.stopPropagation();
                setOpenCard(false);
            }}
            onClick={(e) => {
                e.stopPropagation();
                setOpenCard(false);
            }}
            style={{ padding: "10px" }}
            >X</button>
                </div>           
            </div>
        </Draggable>
    </div>
  );
}

{/* Exportando a função ModalShopping como padrão. */}
export default Horarios;