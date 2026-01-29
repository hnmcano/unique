import { useCarrinho } from "../../contexts/CarrinhoContext";
    
function ProdutosCarrinho() {
    const { atualizarQuantidade, removerProduto, setProdutos, produtos  } = useCarrinho();

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

    return (
        <>
                {/* Lista de produtos no carrinho */}
                <div className="list-products-shopping-cart">
                    {/* Mapeia os produtos no carrinho, e mostra o nome, preco e quantidade */}
                    {produtos.map((p) => (
                        // Cria uma div para cada produto, com o nome, preco e quantidade, como chave o ID do produto
                        <div className="shopping-cart-products" key={p.produto_id}>
                            {/* O nome, preco e quantidade */}
                            <div className="name-products-shopping-cart">{p.nome}</div>
                            <div className="value-and-quantity">
                                {/* O botão para aumentar a quantidade, diminuir a quantidade e remover o produto */}
                                <div className="modify-products-shopping-cart">
                                    {/* botão para aumentar a quantidade */}                                 
                                    <button onClick={() => atualizarQuantidade(p.produto_id, 1)} className="button-quantity-more">+</button>
                                    {/* label para mostrar a quantidade atualizada */}
                                    <label className="quantity-number">{p.quantidade}</label>
                                    {/* botão para diminuir a quantidade */}
                                    <button onClick={() => atualizarQuantidade(p.produto_id, -1)} className="button-quantity-less">-</button>
                                    {/* botão para remover o produto */}    
                                    <button onClick={() => removerProduto(p.produto_id)} className="button-delete-item">&times;</button>
                                </div>
                                <div className="value-products-shopping-cart">
                                    {/* O preco e quantidade vezes a quantidade, fixado em duas casas decimais */}
                                    <label>R${(p.preco_venda * p.quantidade).toFixed(2)}</label>
                                </div>
                            </div>
                        </div>
                    ))}
                    <div style={{flexGrow: 1}}></div>
                </div>
        </>
    );
}

export default ProdutosCarrinho;