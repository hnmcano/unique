// importando a função de estado do react 
import ContainerCategories from "../components/Catalago";
import CadastrarUser from "../components/User";
//import Options from "../components/Options";
import { useEffect, useState } from "react";
import "../styles/HomePage.css"
import { CiBoxList } from "react-icons/ci";
import { GiShoppingCart } from "react-icons/gi";
import { FaRegUserCircle } from "react-icons/fa";
import ModalShopping from "../components/Carrinho";


// Função da pagina principal
function HomePage(){
    const [Categories, setCategories] = useState(true);
    const [optionsOpen, setOptionsOpen] = useState(false);
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [finalizacaoOpen, setFinalizacaoOpen] = useState(false);

    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);


    return (
    <div className="home">
        <div className="options">
            {/* Menu de opções pagina principal, como carrinho, catalogo e finalizar compra*/} 
            <div className="icons-ajustes">
                {/* Icone/Button para abrir catalago caminho componente: /components/Home*/}
                <div className="icons-options">
                    {/* Ao clicar no botão catalogo é enviado o estado do componente para funcao setCategories, dependendo do estado ele será aberto ou fechado  */}
                    <CiBoxList className="icons" onClick={() => { setCategories(true); setFinalizacaoOpen(false);}}/>             
                </div>
                {/*Icone/Button para abrir carrinho, caminho componente: /components/Carrinho, componente será aberto como modal.*/}
                <div className="icons-options">
                    {/* Ao clicar no botão carrinho é enviado o estado do modal para função openModal, dependendo do estado ele será aberto ou fechado  */}
                    <GiShoppingCart onClick={openModal} className="icons"/> <ModalShopping openModal={modalShoppingOpen} closeModal={closeModal}></ModalShopping>                   
                </div>
                {/* Icone/Button para abrir finalizar compra, caminho componente: /components/Finalizacao*/}
                <div className="icons-options" >
                    {/* Ao clicar no botão finalizar compra é enviado o estado do componente para funcao setFinalizacaoOpen, dependendo do estado ele será aberto ou fechado  */}
                    <FaRegUserCircle className="icons" onClick={() => { setCategories(false); setFinalizacaoOpen(true);}} />
                </div>
            </div>
        </div>
        <div className="container">
            {/* Condicional para exibir o componente Home ou finalização de acordo com o botão clicado */}
            {/* Componente Home: /components/Home */}
            {Categories && <ContainerCategories/>}
            {/* Componente Finalizacao: /components/Finalizacao */}
            {!Categories && <CadastrarUser/>}
        </div>
    </div>
);
}

// Exportando a função HomePage como padrão.
export default HomePage;