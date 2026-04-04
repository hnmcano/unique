import ProdutoData from "./DadosProdCatalago";
import { useState} from "react";
import {  useCarrinho } from "../../contexts/CarrinhoContext";

function ListagemProdCatalago({categoria}) {
    const { produtoModalOpen, setProdutoModalOpen } = useCarrinho();
    const [produtoSelecionado, setProdutoSelecionado] = useState(null);
    const diaAtual = (new Date().getDay() + 6) % 7;

    const imagemUrl = (imagem) => `data:image/png;base64,${imagem}`;

    const handleProdutoClick = (produto) => {
        setProdutoSelecionado(produto);
        setProdutoModalOpen(true);
        console.log(produto);
    };

    const closeModalProduto = () => {
        setProdutoModalOpen(false);
        setProdutoSelecionado(null);
    };

    return (    
        <div className="products-gouped">             
            <ProdutoData
                open={produtoModalOpen}
                closeModalProduto={closeModalProduto}
                produto={produtoSelecionado}
                categoria={categoria}
            ></ProdutoData>
            {categoria.produtos
                .filter(produto => produto.dias_vendas === null || produto.dias_vendas === diaAtual)
                .map((produto) => (
                    <div key={produto.id} className="produtos-item" onClick={() => handleProdutoClick(produto)}>
                        <div className="data-itens-product">
                            <div className="data-img-container">
                                <img className="img-product" src={imagemUrl(produto.imagem)} alt="imagem produto"/>
                            </div>
                            <div className="data-description-container">
                                <div>{produto.nome}</div>
                                <div className="data-description">
                                    {produto.descricao}
                                </div>
                            </div>
                        </div>
                    </div>
                ))
            }
        </div>
    );
}

export default ListagemProdCatalago;