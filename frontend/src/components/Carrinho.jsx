// importando as funções de estado, referencia e efeitos do React
import React, { useRef, useState, useEffect} from "react";
// importando axios, função de requisições HTTP
import axios from "axios";
// importando estilo do modal carrinho em ".css"
import "../styles/Carrinho.css"
// importando função de Draggable para referenciar no DOM e permitir arrastar o modal
import Draggable from "react-draggable";
// importando hook de carrinho, que contem as funções para manipular o carrinho.
import { useCarrinho} from "../hooks/useCarrinho";
import { Link } from "react-router-dom";


// Função principal do modal carrinho, recebendo o estado de abertura e fechamento do modal
function ModalShopping({closeModal, openModal, children}){
    // definindo estado de total de produtos no carrinho como 0
    const [total, setTotal] = useState(0);
    // importando hooks (caminho: src/hooks/useCarrinho ) de carrinho que contem as funções para manipular o carrinho, como produtos, 
    // deletar todos os produtos, quantidade de produtos e remover produto.
    const { produtos, setProdutos, delCartShopping, isLoading, fetchCarrinho, quantidadeItems, removerProduto  } = useCarrinho();

    // definindo referencia para o modal como null
    const nodeRef = useRef(null);
    
    // Efeito para ao abrir o modal, buscar os dados do carrinho
    useEffect(() => {
        // se o modal for aberto, buscar os dados do carrinho
        if (openModal) {
            fetchCarrinho();  
        }
    }, [openModal, fetchCarrinho]);

    //Somar o total por produtos e quantidade
    const handleQuantidade = async(id, delta) => {
        // Pega a os dados atuais dos produtos do carrinho e atualiza a quantidade
        setProdutos(prev => {
        // define uma variavel que irá receber a nova quantidade sem alterar o estado original
        // Realiza um mapeamento de todos os produtos do carrinho do estado original, e o p retorna o produto e todos os seu dados
        const novaQuantidade = prev.map(p =>
            // Verifica se o produto original tem o mesmo id do produto clicado
            p.produto_id === id 
            // Se sim, copia todas as propriedades do produto atual e atualiza a propriedade quantidade, 
            // com a quantidade atual + delta (que poder ser tanto +1 quanto -1), Math.max(1) garante que a quantidade nunca seja igual a 0 ou negativa
            ? {...p, quantidade: Math.max(1, p.quantidade + delta) } 
            // Se não, retorna o produto original
            : p
        );

        // a variavel 'produtoAtualizado' recebe uma copia do produto atualizado, realizando uma busca no array 'novaQuantidade'
        // validando se o produto atualizado tem o mesmo id do produto clicado
        const produtoAtualizado = novaQuantidade.find(p => p.produto_id === id);

        // Realiza uma requisição HTTP para atualizar a propriedade quantidade do produto no carrinho (tabela definida no SQLlite, requisição PUT rota FastApi)
        // No cabeçalho da requisição, define o header 'Content-Type' como 'application/json'
        // Dados enviados no corpo da requisição, o produto atualizado
        axios.put(`http://127.0.0.1:8000/carrinho/atualizar/quantidade/${id}/${produtoAtualizado.quantidade}`, { produtoAtualizado })
        // Se a requisição for bem-sucedida, imprime uma mensagem de sucesso no console
        .then(response => {
            console.log('Quantidade atualizada com sucesso:', response.data);
        })
        // Se a requisição falhar, imprime uma mensagem de erro no console
        .catch(error => {
            // Imprime a mensagem de erro no console, juntamente com os dados do produto atualizado
            console.log('Resposta do servidor:', produtoAtualizado);
            // Imprime o erro no console, juntamente com a mensagem de erro
            console.error('Erro ao atualizar a quantidade:', error);
        });
        // Retorna a nova quantidade
        return novaQuantidade;

        });
    }

    //Calcular o total
    useEffect(() => {
        // se o modal for aberto, calcular o total
        if(openModal){
            // Realiza um mapeamento dos produtos no carrinho, e soma o preco_venda * quantidade
            // De acordo com que as dependencias tenham modificações
            const soma = produtos.reduce((acc, p) => acc + (p.preco_venda * p.quantidade), 0);
            // Altera o estado do total
            setTotal(soma);
        }
        // Dependencias, baseadas nos produtos e se o modal estiver aberto, para calcular o total
    }, [produtos, openModal]);


    // Função para remover produto de forma assincrona, com base no ID do produto
    const handleRemover = async (produto_id) => {
        // Realiza uma requisição HTTP para remover o produto do carrinho (tabela definida no SQLlite, requisição DELETE rota FastApi)
        try {
            // Aguardar a requisição ser concluida, função onde contém a requisição HTTP está no caminho: src/hooks/useCarrinho.js
            await removerProduto(produto_id);
            // Após a requisição ser concluida, é removido o produto do carrinho com filtro no estado
            setProdutos(prev => prev.filter(p => p.produto_id !== produto_id));
            // Se a requisição for bem-sucedida, imprime uma mensagem de sucesso no console
            console.log('Produto removido com sucesso');
        } catch (error) {
            // Se a requisição falhar, imprime uma mensagem de erro no console
           console.error('Erro ao remover:', error);
        }
    };

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
                    {/* O botão de fechar */}
                    <button className="modal-close-btn" onClick={closeModal}>&times;</button> 
                </div>
                
                {/* O conteúdo que for passado (ex: seu formulário) */}
                {children}

                {/* Lista de produtos no carrinho */}
                <div className="listproductsshoppingcart">
                    {/* Mapeia os produtos no carrinho, e mostra o nome, preco e quantidade */}
                    {produtos.map((p) => (
                        // Cria uma div para cada produto, com o nome, preco e quantidade, como chave o ID do produto
                        <div className="shoppingcartproducts" key={p.produto_id}>
                            {/* O nome, preco e quantidade */}
                            <div className="nameproductsshoppingcart">{p.nome}</div>
                            <div className=""></div>
                            <div className="valueproductsshoppingcart">
                            {/* O preco e quantidade vezes a quantidade, fixado em duas casas decimais */}
                            <label>R${(p.preco_venda * p.quantidade).toFixed(2)}</label>
                            </div>
                            {/* O botão para aumentar a quantidade, diminuir a quantidade e remover o produto */}
                            <div className="modifyproductsshoppingcart">
                            {/* botão para aumentar a quantidade */}                                 
                            <button onClick={() => handleQuantidade(p.produto_id, 1)} className="buttonquantitymore">+</button>
                            {/* label para mostrar a quantidade atualizada */}
                            <label className="quantity-number">{p.quantidade}</label>
                            {/* botão para diminuir a quantidade */}
                            <button onClick={() => handleQuantidade(p.produto_id, -1)} className="buttonquantityless">-</button>
                            {/* botão para remover o produto */}    
                            <button onClick={() => handleRemover(p.produto_id)} className="buttondeleteitem">-</button>
                            </div>
                        </div>
                    ))}
                    <div style={{"flex-grow": "1"}}></div>
                </div>
                {/* Rodapé do modal */}
                <div className="modal-footer">
                    {/* O total por valores e quantidade de produtos unicos */}
                    <div className="totalvalueshoppingcart">
                        {/* label para o total por valor */}
                        <label className="totalvalueshoppingcart">Total: R$ {total.toFixed(2)}</label>
                        {/* label para a quantidade de produtos no carrinho (unicos) */}
                        <label className="totalvalueshoppingcart">Qtd: {quantidadeItems}</label>
                    </div>
                    {/* Botão para finalizar compra */}
                    <Link to="/conclusao">
                        <button onClick={() => closeModal()} className="buttonfinishbuy">Finalizar Compra</button>
                    </Link>
                    {/* Botão para excluir carrinho */}
                    <button onClick={() => delCartShopping()} className="buttonfinishcancel" disabled={isLoading}>Excluir Carrinho</button>
                </div>
            </div>
        </Draggable>
    </div>
  );
}

{/* Exportando a função ModalShopping como padrão. */}
export default ModalShopping;