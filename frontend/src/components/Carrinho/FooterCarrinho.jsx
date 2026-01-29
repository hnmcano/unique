import BotaoFinalizacao from "./BotaoFinalizarCarrinho";
import { useCarrinho } from "../../contexts/CarrinhoContext";
import React, { useState, useEffect } from "react";

function FooterCarinho({closeModal, openModal}) {
    const { produtos, totalCarrinho } =  useCarrinho();

    return (
        <>
            {/* Rodapé do modal */}
            <div className="modal-footer">
                {/* O total por valores e quantidade de produtos unicos */}
                <div className="total-values-shopping-cart">
                    {/* label para o total por valor */}
                    <div>
                        <label className="total-value-shopping-cart-total">Total: R$ {totalCarrinho.toFixed(2)}</label>
                    </div>
                    {/* label para a quantidade de produtos no carrinho (unicos) */}
                    <div>
                        <label className="total-values-shopping-cart-qtd">Qtd: {produtos.length}</label>
                    </div>
                </div>
                {/* Botão para finalizar compra */}
                <BotaoFinalizacao 
                    closeModal={closeModal}
                />
            </div>
        </>
    );

}

export default FooterCarinho;