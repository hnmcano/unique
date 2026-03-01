// importando as funções de estado, referencia e efeitos do React
import { useRef, useEffect} from "react";

// importando commponents do modal
import ProdutosCarrinho from "../components/Carrinho/ProdutosCarrinho";
import FooterCarrinho from "../components/Carrinho/FooterCarrinho";

// importando hooks de carrinho
import {useCarrinho } from "../hooks/useCarrinho";

// importando estilo do modal carrinho em ".css"
import "../styles/Carrinho.css"

// importando função de Draggable para referenciar no DOM e permitir arrastar o modal
import Draggable from "react-draggable";

// Função principal do modal carrinho, recebendo o estado de abertura e fechamento do modal
function Carrinho({closeModal, openModal, children}){
    // definindo estado de total de produtos no carrinho como 0
    
    // importando hooks (caminho: src/hooks/useCarrinho ) de carrinho que contem as funções para manipular o carrinho, como produtos, 
    // deletar todos os produtos, quantidade de produtos e remover produto.
    const { produtos, fetchCarrinho, quantidadeItems } = useCarrinho();

    // definindo referencia para o modal como null
    const nodeRef = useRef(null);
    
    // Efeito para ao abrir o modal, buscar os dados do carrinho
    useEffect(() => {
        // se o modal for aberto, buscar os dados do carrinho
        if (openModal) {
            fetchCarrinho();  
        }
    }, [openModal, fetchCarrinho]);


    // Se o modal não estiver aberto, retorna null
    if (!openModal) return null;

    return (
    // Modal de carrinho
    <div className="modal-overlay" onClick={closeModal}>
        {/* O Modal pode ser arrastado devido a biblioteca Draggable com o nodeRef */}
        <Draggable nodeRef={nodeRef} handle=".modal-header-handle" bounds="parent">
            {/* Com o nodeRef estamos referenciando o modal, permitindo arrastar o modal, 
            onclick={(e) => e.stopPropagation()} impede que o modal seja fechado ao clicar no conteúdo */}
            <div ref={nodeRef} className="modal-content" onClick={(e) => e.stopPropagation()}>
                {/* O cabeçalho do modal */}
                <div className="modal-header-handle">
                    {/* O cabeçalho do modal contém o título e o botão de fechar */}
                    <label className="titleproductsshoppingcart">Carrinho de Compras</label>
                </div>
                
                {/* O conteúdo que for passado (ex: seu formulário) */}
                {children}

                <ProdutosCarrinho />
                <FooterCarrinho 
                    openModal={openModal}
                    closeModal={closeModal}
                />           
            </div>
        </Draggable>
    </div>
  );
}

{/* Exportando a função ModalShopping como padrão. */}
export default Carrinho;