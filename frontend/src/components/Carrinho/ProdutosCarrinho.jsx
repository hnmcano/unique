import { useCarrinho} from "../../hooks/useCarrinho";
    
function ProdutosCarrinho() {
    const { produtos, setProdutos, removerProduto  } = useCarrinho();

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
            api.put(`/carrinho/atualizar/quantidade/${id}/${produtoAtualizado.quantidade}`, { produtoAtualizado })
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
                                    <button onClick={() => handleQuantidade(p.produto_id, 1)} className="button-quantity-more">+</button>
                                    {/* label para mostrar a quantidade atualizada */}
                                    <label className="quantity-number">{p.quantidade}</label>
                                    {/* botão para diminuir a quantidade */}
                                    <button onClick={() => handleQuantidade(p.produto_id, -1)} className="button-quantity-less">-</button>
                                    {/* botão para remover o produto */}    
                                    <button onClick={() => handleRemover(p.produto_id)} className="button-delete-item">&times;</button>
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