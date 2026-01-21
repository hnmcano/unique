import React, { useEffect, useState } from "react";
import "../styles/ProdutoData.css"
import api from "../api/api";
import { useProdutos } from "../hooks/useProdutos";
import { useCarrinho } from "../hooks/useCarrinho";
import Button_market from "../components/Button_market";

function ProdutoData({ open, closeModalProduto, produto, categoria}) {
    const [quantidade, setQuantidade] = useState(1);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleQuantidade = (delta) => {
        setQuantidade(prevQuantidade => {
            const novaQuantidade = prevQuantidade + delta;
            return novaQuantidade < 1 ? 1 : novaQuantidade;
        });
    }

    const addProduct =  async (categoria, produto) => {
        
        setLoading(true);
        setError(null);

        const dadosEnviar = {
            produto_id: produto.produto_id,
            cod_pdv: produto.cod_pdv,
            nome: produto.nome,
            categoria: categoria.nome_categoria,
            preco_custo: produto.preco_custo,
            preco_venda: produto.preco_venda,
            medida: produto.medida,
            estoque: produto.estoque,
            estoque_min: produto.estoque_min,
            sit_estoque: produto.sit_estoque,   
            descricao: produto.descricao,
            ficha_tecnica: produto.ficha_tecnica,
            status_venda: produto.status_venda,
            imagem_url: produto.imagem,
            quantidade: quantidade
        };

        console.log('Dados a enviar:',dadosEnviar);

        try {
            const response = await api.post(`/carrinho/adicionar-produto/${produto.produto_id}`, dadosEnviar);
            alert('Produto adicionado ao carrinho com sucesso!');
            console.log('Resposta do servidor:', response.data);
            const {qtd} = await fetchCarrinho();
            console.log('Quantidade atualizada de itens no carrinho:', qtd);

        } catch (error) {
            console.error('Erro ao enviar os dados:', error);
            setError(error.message);
            console.error('Erro ao enviar os dados:', dadosEnviar);
        } finally {
            setLoading(false);
        }

    }

    const imagem_url = (imagem) => `data:image/png;base64,${imagem}`;


    if (!open || !produto) return null;

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
                        <button onClick={() => addProduct(categoria, produto)} className="beautiful-button">Adicionar</button>
                    </div>
                </div>
            </div>
        </div>  
    );


};

export default ProdutoData;