import React, { useState } from "react";
import { GiShoppingCart } from "react-icons/gi";
import Carrinho from "../../pages/Carrinho";
import { useCarrinho } from "../../contexts/CarrinhoContext";

function BotaoCarrinho({MenuOpen, quantidade}) {
    const { produtoModalOpen, setProdutoModalOpen } = useCarrinho();
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);

    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);

    return (
        <>
            { !modalShoppingOpen && !MenuOpen && !produtoModalOpen && (
                <button className="button-shopping-cart">
                    <GiShoppingCart onClick={openModal} className="icons"/> <span className="quantidade-botao-carrinho">{quantidade}</span>
                </button>
            )}
            <Carrinho openModal={modalShoppingOpen} closeModal={closeModal}></Carrinho>
        </>
    );
}

export default BotaoCarrinho;