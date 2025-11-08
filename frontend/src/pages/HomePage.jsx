import React, { useState } from "react";
import "../styles/HomePage.css"
import ModalShopping from "../components/Carrinho";
import ContainerCategories from "../components/categorias";
import { GiShoppingCart } from "react-icons/gi";
import { CiBoxList } from "react-icons/ci";
import { FaRegUserCircle } from "react-icons/fa";
import { useProdutos } from "../hooks/useProdutos";



function HomePage(){
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [categories, setCategories] = useState(false);
    const { base: setBaseProdutos } = useProdutos();

    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);

    const toggleMenu = () => {
        setMenuOpen((prevState) =>  !prevState);
    };

    return (
    <div className="home">
        <div className="options">
            <div className="icons-ajustes">
                <div className="icons-options">
                    <CiBoxList className="icons" onClick={() => setCategories(!categories)}/>             
                </div>
                <div className="icons-options">
                    <GiShoppingCart onClick={openModal} className="icons"/>
                    <ModalShopping 
                        openModal={modalShoppingOpen} 
                        closeModal={closeModal}>
                    </ModalShopping>                   
                </div>
                <div className="icons-options" >
                    <FaRegUserCircle className="icons" style={{width: "30px", height: "30px"}}  />

                </div>
                <div className="icons-options">           
                </div>
                <div className="icons-options">                
                </div>
            </div>
        </div>
        <div className="container">
            <div className="header">
                <div className="logotipo-hookah">
                    <img src="/src/assets/logo_hookahshisha.png" alt="Logo" className="logo"/>
                </div>
                <div className="data"></div>
                <div className="buttons-filters">
                    {setBaseProdutos && setBaseProdutos.map((categoria, index) => (
                        <button className="buttons-filters">{categoria.categoria}</button>
                    ))}
                </div>
            </div>
            <div className="container__">
                {categories && <ContainerCategories/>}
            </div>
        </div>
    </div>
);
}

export default HomePage;