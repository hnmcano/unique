import ProdutoData from "./DadosProdCatalago";
import { useState} from "react";

function ListagemProdCatalago({categoria}) {
    const [modalOpenProduto, setModalOpenProduto] = useState(false);
    const [produtoSelecionado, setProdutoSelecionado] = useState(null);

    const imagemUrl = (imagem) => `data:image/png;base64,${imagem}`;

    const handleProdutoClick = (produto) => {
        setProdutoSelecionado(produto);
        setModalOpenProduto(true);
        console.log(produto);
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
                categoria={categoria}
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
                    </div>
                </div>
            </div>
            ))}
        </div>
    );
}

export default ListagemProdCatalago;