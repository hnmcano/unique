import React, { useState } from "react";
import "../styles/HomePage.css"
import ModalShopping from "../components/Carrinho";
import ContainerCategories from "../components/Home";
import DataFinalizacao from "../components/Finalizacao";
import { GiShoppingCart } from "react-icons/gi";
import { CiBoxList } from "react-icons/ci";
import { FaRegUserCircle} from "react-icons/fa";


function HomePage(){
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [Categories, setCategories] = useState(true);
    const [FinalizacaoOpen, setFinalizacaoOpen] = useState(false);
    
    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);

    return (
    <div className="home">
        <div className="options">
            <div className="icons-ajustes">
                <div className="icons-options">
                    <CiBoxList className="icons" onClick={() => { setCategories(true); setFinalizacaoOpen(false);}}/>             
                </div>
                <div className="icons-options">
                    <GiShoppingCart onClick={openModal} className="icons"/>
                    <ModalShopping 
                        openModal={modalShoppingOpen} 
                        closeModal={closeModal}>
                    </ModalShopping>                   
                </div>
                <div className="icons-options" >
                    <FaRegUserCircle className="icons" onClick={() => { setCategories(false); setFinalizacaoOpen(true);}} />

                </div>
                <div className="icons-options">           
                </div>
                <div className="icons-options">                
                </div>
            </div>
        </div>
        <div className="container">
            {Categories && <ContainerCategories/>}
            {FinalizacaoOpen && <DataFinalizacao/>}
        </div>
    </div>
);
}

export default HomePage;