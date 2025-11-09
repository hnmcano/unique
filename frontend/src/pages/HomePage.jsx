import React, { useState } from "react";
import "../styles/HomePage.css"
import ModalShopping from "../components/Carrinho";
import ContainerCategories from "../components/Home";
import DataClient from "../components/Cliente";
import { GiShoppingCart } from "react-icons/gi";
import { CiBoxList } from "react-icons/ci";
import { FaRegUserCircle} from "react-icons/fa";


function HomePage(){
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [Categories, setCategories] = useState(true);
    const [ClientOpen, setClientOpen] = useState(false);
    
    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);

    return (
    <div className="home">
        <div className="options">
            <div className="icons-ajustes">
                <div className="icons-options">
                    <CiBoxList className="icons" onClick={() => { setCategories(true); setClientOpen(false);}}/>             
                </div>
                <div className="icons-options">
                    <GiShoppingCart onClick={openModal} className="icons"/>
                    <ModalShopping 
                        openModal={modalShoppingOpen} 
                        closeModal={closeModal}>
                    </ModalShopping>                   
                </div>
                <div className="icons-options" >
                    <FaRegUserCircle className="icons" onClick={() => { setCategories(false); setClientOpen(true);}} />

                </div>
                <div className="icons-options">           
                </div>
                <div className="icons-options">                
                </div>
            </div>
        </div>
        <div className="container">       
            {Categories && <ContainerCategories/>}
            {ClientOpen && <DataClient/>}
        </div>
    </div>
);
}

export default HomePage;