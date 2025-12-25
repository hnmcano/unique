import React, { useState, useEffect } from "react";
import "../styles/ProdutoData.css"

function ProdutoData({ open, closeModalProduto, produto }) {

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

    if (!open || !produto) return null;

    return (
        <div className="modal-overlay" onClick={closeModalProduto}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                <div className="modal-header-produto-data">
                    <h2>{produto.nome}</h2>
                </div>
                <div className="modal-body-produto-data">
                    <p>{produto.descricao}</p>
                </div>
                <div className="modal-footer-produto-data">
                    <button onClick={closeModalProduto}>Fechar</button>
                </div>
            </div>
        </div>  
    );


};

export default ProdutoData;