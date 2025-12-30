import React, { useState, useEffect } from "react";
import "../styles/ProdutoData.css"

function ProdutoData({ open, closeModalProduto, produto }) {
    const [quantidade, setQuantidade] = useState(1);
    const [novaQuantidade, setNovaQuantidade] = useState(1);

    if (!open || !produto) return null;

    const imagem_url = (imagem) => `data:image/png;base64,${imagem}`;

    const handleQuantidade = (delta) => {
        setQuantidade(prevQuantidade => {
            const novaQuantidade = prevQuantidade + delta;
            return novaQuantidade < 1 ? 1 : novaQuantidade;
        });
    }       

    return (
        <div className="modal-overlay" onClick={closeModalProduto}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                <div onClick={closeModalProduto} className="styled-wrapper">
                    <button className="button">
                        <div className="button-box">
                        <span className="button-elem">
                            <svg
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                            className="arrow-icon"
                            >
                            <path
                                fill="black"
                                d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"
                            ></path>
                            </svg>
                        </span>
                        <span className="button-elem">
                            <svg
                            fill="black"
                            viewBox="0 0  24 24"
                            xmlns="http://www.w3.org/2000/svg"
                            className="arrow-icon"
                            >
                            <path
                                d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"
                            ></path>
                            </svg>
                        </span>
                        </div>
                    </button>
                </div>
                <div>
                    <img className="imagem-product-data" src={imagem_url(produto.imagem)}></img>
                </div>
                <div className="dados-produto-data">
                    <div className="modal-name-produto-data">
                        <h2>{produto.nome}</h2>
                    </div>
                    <div className="modal-descricao-produto-data">
                        <p>{produto.descricao}</p>
                    </div>
                    <div className="modal-preco-produto-data">
                        <label>R$</label>
                        <label>{(quantidade * produto.preco_venda).toFixed(2)}</label>
                    </div>
                    <div className="quantidade-product-cart">
                        <div className="adicionar-carrinho">
                            <label onClick={() => handleQuantidade(1)} className="modifique">+</label>
                        </div>
                        <div className="contagem-quantidade">{quantidade}</div>
                        <div className="remover-carrinho">
                            <label onClick={() => handleQuantidade(-1)} className="modifique">-</label>
                        </div>
                    </div>
                    <div className="modal-footer-produto-data">
                        <button className="beautiful-button">Adicionar</button>
                    </div>
                </div>
            </div>
        </div>  
    );


};

export default ProdutoData;