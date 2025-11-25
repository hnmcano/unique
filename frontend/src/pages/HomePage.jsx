// importando a função de estado do react 
import React, { useState } from "react";
// importando estilo de pagina ".css" da pagina principal
import "../styles/HomePage.css"
// importando componente carrinho
import ModalShopping from "../components/Carrinho";
// importando componente categorias
import ContainerCategories from "../components/Home";
// importando componente finalizacao
import DataFinalizacao from "../components/Finalizacao";

// importando icones da pagina https://react-icons.github.io/react-icons/
// icone catalago
import { GiShoppingCart } from "react-icons/gi";
// icone carrinho
import { CiBoxList } from "react-icons/ci";
// icone finalizar compra
import { FaRegUserCircle} from "react-icons/fa";

// Função da pagina principal
function HomePage(){
    // Estabelecendo estado do modal carrinho como falso, ou seja fechado, para ser aberto quando o botão de carrinho for clicado.
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    // estabelecendo estado do componente categorias como true, ou seja evidenciado, para ser exibido assim que a página for carregada
    const [Categories, setCategories] = useState(true);
    // estabelecendo estado do componente finalizacao como falso, ou seja fechado, 
    // para ser exibido assim que o botão de finalizar compra for clicado no carrinho ou no menu opções
    const [FinalizacaoOpen, setFinalizacaoOpen] = useState(false);
    
    // Funções para abrir e fechar o modal carrinho
    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);

    // Retorno da pagina principal
    return (
    <div className="home">
        {/* Menu de opções pagina principal, como carrinho, catalogo e finalizar compra*/} 
        <div className="options">
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
        {/* Container principal onde serão exibidos os componentes, 
        sendo eles: /components/Home e /components/Finalizacao de acordo com o botão clicado*/}
        <div className="container">
            {/* Condicional para exibir o componente Home ou finalização de acordo com o botão clicado */}
            {/* Componente Home: /components/Home */}
            {Categories && <ContainerCategories/>}
            {/* Componente Finalizacao: /components/Finalizacao */}
            {FinalizacaoOpen && <DataFinalizacao/>}
        </div>
    </div>
);
}

// Exportando a função HomePage como padrão.
export default HomePage;