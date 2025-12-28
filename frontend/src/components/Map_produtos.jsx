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
    
    // const [loading, setLoading] = useState(false);
    // const [error, setError] = useState(null);


    // const addProduct =  async (categoria, produtos) => {

    //     console.log(produtos);

    //     setLoading(true);
    //     setError(null);

    //     const dadosEnviar = {
    //         produto_id: produtos.produto_id,
    //         cod_pdv: produtos.cod_pdv,
    //         nome: produtos.nome,
    //         categoria: categoria.nome_categoria,
    //         preco_custo: produtos.preco_custo,
    //         preco_venda: produtos.preco_venda,
    //         medida: produtos.medida,
    //         estoque: produtos.estoque,
    //         estoque_min: produtos.estoque_min,
    //         sit_estoque: produtos.sit_estoque,
    //         descricao: produtos.descricao,
    //         ficha_tecnica: produtos.ficha_tecnica,
    //         status_venda: produtos.status_venda,
    //         imagem_url: produtos.imagem_url,
    //         quantidade: 1
    //     };

    //     console.log('Dados a enviar:',dadosEnviar);

    //     try {
    //         const response = await axios.post(`http://127.0.0.1:8000/carrinho/adicionar-produto/${produtos.produto_id}`, dadosEnviar);
    //         console.log('Resposta do servidor:', response.data);
    //     } catch (error) {
    //         console.error('Erro ao enviar os dados:', error);
    //         setError(error.message);
    //         console.error('Erro ao enviar os dados:', dadosEnviar);
    //     } finally {
    //         setLoading(false);
    //     }
    // }
    
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