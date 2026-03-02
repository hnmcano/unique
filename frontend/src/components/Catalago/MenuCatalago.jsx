import React, { useEffect, useState } from "react";
import { CiBoxList } from "react-icons/ci";
import { GiShoppingCart } from "react-icons/gi";
import Carrinho from "../../pages/Carrinho";
import "../../styles/MenuCatalago.css";


import { useCarrinho } from "../../contexts/CarrinhoContext";

function Options( { setCategories, MenuOpen, setMenuOpen }) {
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [finalizacaoOpen, setFinalizacaoOpen] = useState(false);
    const { produtos } = useCarrinho();

    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);
    if (!setMenuOpen) return null;

    return (
        <>
        { MenuOpen && ( <div className="overlay" onClick={() =>  setMenuOpen(false)}/>)}
        <aside className={`options ${MenuOpen ? "open" : ""}`}>
            {/* Menu de opções pagina principal, como carrinho, catalogo e finalizar compra*/} 
            <div className="icons-ajustes">
                <div className="icons-options">
                    {/* Icone/Button para abrir catalago caminho componente: /components/Home*/}
                    <div className="options-container-name-icons">
                        {/* Ao clicar no botão catalogo é enviado o estado do componente para funcao setCategories, dependendo do estado ele será aberto ou fechado  */}
                        <CiBoxList className="icons" onClick={() => { setCategories(true); setFinalizacaoOpen(false);}}/>
                        <span className="name-menu">Catalogo</span>                                     
                    </div>
                </div>  
                {/*Icone/Button para abrir carrinho, caminho componente: /components/Carrinho, componente será aberto como modal.*/}
                <div className="icons-options"> 
                    <div className="options-container-name-icons">
                        {/* Ao clicar no botão carrinho é enviado o estado do modal para função openModal, dependendo do estado ele será aberto ou fechado  */}
                        <GiShoppingCart onClick={openModal} className="icons"/> <Carrinho openModal={modalShoppingOpen} closeModal={closeModal}></Carrinho>
                        <span className="name-menu">Carrinho</span>                                           
                    </div>
                </div>
                {/* Icone/Button para abrir finalizar compra, caminho componente: /components/Finalizacao*/}
                <div className="icons-options">
                </div>
                <div style={{"flexGrow": "1"}}></div>
                <div className="div-button-login">
                    <div
                        aria-label="User Login Button"
                        tabindex="0"
                        role="button"
                        class="user-profile"
                        >
                        <div className="user-profile-inner">
                            <svg
                            aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            >
                            <g data-name="Layer 2" id="Layer_2">
                                <path
                                d="m15.626 11.769a6 6 0 1 0 -7.252 0 9.008 9.008 0 0 0 -5.374 8.231 3 3 0 0 0 3 3h12a3 3 0 0 0 3-3 9.008 9.008 0 0 0 -5.374-8.231zm-7.626-4.769a4 4 0 1 1 4 4 4 4 0 0 1 -4-4zm10 14h-12a1 1 0 0 1 -1-1 7 7 0 0 1 14 0 1 1 0 0 1 -1 1z"
                                ></path>
                            </g>
                            </svg>
                            <p>Log In</p>
                        </div>
                    </div>
                </div>
            </div>
        </aside>
        </>
    );
}


export default Options;