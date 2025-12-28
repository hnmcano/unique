import React, { useState, useEffect } from "react";
import "../styles/ProdutoData.css"

function ProdutoData({ open, closeModalProduto, produto }) {

    if (!open || !produto) return null;

    const imagem_url = (imagem) => `data:image/png;base64,${imagem}`;

    return (
        <div className="modal-overlay" onClick={closeModalProduto}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
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
                        <label style={{"width": "90vw", "text-align": "right"}}>{produto.preco_venda.toFixed(2)}</label>
                    </div>
                    <div className="quantidade-product-cart">
                        <div className="adicionar-carrinho">
                            <label className="modifique">+</label>
                        </div>
                        <div className="contagem-quantidade">1</div>
                        <div className="remover-carrinho">
                            <label className="modifique">-</label>
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