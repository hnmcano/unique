import { useCarrinho } from "../../contexts/CarrinhoContext";
    
function ProdutosCarrinho() {
    const { atualizarQuantidade, removerProduto, produtos } = useCarrinho();

    return (
        <>
            <div className="list-products-shopping-cart">
                {produtos.map((p) => (
                    <div 
                        className="shopping-cart-products" 
                        key={`${p.produto_id}-${p.tamanho || "unico"}`}
                    >
                        <div className="name-products-shopping-cart">
                            {p.nome}
                            {p.tamanho && ` (${p.tamanho})`}
                        </div>

                        <div className="value-and-quantity">
                            <div className="modify-products-shopping-cart">

                                <button 
                                    onClick={() => atualizarQuantidade(p.id_item, 1)}  
                                    className="button-quantity-more"
                                >
                                    +
                                </button>

                                <label className="quantity-number">
                                    {p.quantidade}
                                </label>

                                <button 
                                    onClick={() => atualizarQuantidade(p.id_item, -1)} 
                                    className="button-quantity-less"
                                >
                                    -
                                </button>

                                <button 
                                    onClick={() => removerProduto(p.id_item)}  
                                    className="button-delete-item"
                                >
                                    &times;
                                </button>
                            </div>

                            <div className="value-products-shopping-cart">
                                <label>
                                    R${(p.preco_venda * p.quantidade).toFixed(2)}
                                </label>
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