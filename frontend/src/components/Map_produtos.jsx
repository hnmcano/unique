import ProdutoData from "./ProdutoData";
import React, { useState, useEffect} from "react";

function ProdutosAcionados({categoria}) {
    const [modalOpenProduto, setModalOpenProduto] = useState(false);
    const [produtoSelecionado, setProdutoSelecionado] = useState(null);

    const imagemUrl = (imagem) => `data:image/png;base64,${imagem}`;

    const handleProdutoClick = (produto) => {
        console.log('Produto clicado:', produto);
        setProdutoSelecionado(produto);
        setModalOpenProduto(true);
    };

    const closeModalProduto = () => {
        setModalOpenProduto(false);
        setProdutoSelecionado(null);
    };

    
    return (    
        <div className="products-gouped">             
            <ProdutoData
                open={modalOpenProduto}
                closeModalProduto={closeModalProduto}
                produto={produtoSelecionado}
            ></ProdutoData>
            {categoria.produtos.map((produto) => (
            <div key={produto.produto_id} className="produtos-item" onClick={() => handleProdutoClick(produto)}>
                <div className="data-itens-product">
                    <div className="data-img-container">
                        <img className="img-product" src={imagemUrl(produto.imagem)} alt="imagem produto"/>
                    </div>
                    <div className="data-description-container">
                        <div>
                            {produto.nome}
                        </div>
                        <div className="data-description">
                            {produto.descricao}
                        </div>
                        <div>
                            <div className="data-adicionar-container">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            ))}
        </div>
    );
}

export default ProdutosAcionados;