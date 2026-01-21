import React, { useState } from "react";
import { CiBoxList } from "react-icons/ci";
import { GiShoppingCart } from "react-icons/gi";
import { FaRegUserCircle } from "react-icons/fa";
import ModalShopping from "../components/Carrinho";
import "../styles/Options.css"

function Options( { setCategories, MenuOpen, setMenuOpen }) {
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [finalizacaoOpen, setFinalizacaoOpen] = useState(false);

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
                    <div onClick={openModal} className="options-container-name-icons">
                        {/* Ao clicar no botão carrinho é enviado o estado do modal para função openModal, dependendo do estado ele será aberto ou fechado  */}
                        <GiShoppingCart className="icons"/> <ModalShopping openModal={modalShoppingOpen} closeModal={closeModal}></ModalShopping>
                        <span className="name-menu">Carrinho</span>                                           
                    </div>
                </div>
                {/* Icone/Button para abrir finalizar compra, caminho componente: /components/Finalizacao*/}
                <div className="icons-options">
                    <div onClick={() => { setCategories(false); setFinalizacaoOpen(true);}} className="options-container-name-icons">
                        {/* Ao clicar no botão finalizar compra é enviado o estado do componente para funcao setFinalizacaoOpen, dependendo do estado ele será aberto ou fechado  */}
                        <FaRegUserCircle className="icons"/>
                        <span className="name-menu">Usuario</span>
                        
                    </div>
                </div>
            </div>
        </aside>
        </>
    );
}


export default Options;