import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/HomePage.css"
import ProdutosAcionados from "../components/produtos";
import ModalShopping from "../components/Carrinho";
import { GiShoppingCart } from "react-icons/gi";


function HomePage(){
    const [base, setBase] = useState(null);
    const [categoriaVisible, setCategoriaVisible] = useState({});
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);

    const openModal = () => setModalShoppingOpen(true);
    const closeModal = () => setModalShoppingOpen(false);
    
    const toggleVisibility = (index) => {
        // Converte o índice para string, se necessário, para ser uma chave de objeto consistente
        const indexString = String(index); 
        
        setCategoriaVisible((prevState) => ({
            ...prevState,
            // Usa o índice como chave no estado
            [indexString]: !prevState[indexString],
        }));
    };

    const toggleMenu = () => {
        setMenuOpen((prevState) =>  !prevState);
    };

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/products/react/produtos")
            .then(response => {
                setBase(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
    }, []);

    return (
    <div className="container_principal">
        <div className="menusuperior">
            <div className="filter">
                <label>Buscar</label>
                <input type="text" />
                <button>Filtrar</button>
            </div>
            <div className="buttonsuperior">
                <div >
                    <GiShoppingCart onClick={openModal} className="iconShoppingCart" />
                </div>
                <ModalShopping 
                openModal={modalShoppingOpen} 
                closeModal={closeModal}>
                </ModalShopping>                   
            </div>
        </div>
        <div className="container_products">
            <div className="categorias">
                {base && base.map((categoria, index) => (
                    <div key={index}>
                    <div className="produtos" onClick={() => toggleVisibility(index)}>{categoria.categoria}</div>
                        <div>
                            {categoriaVisible[String(index)] && ( <ProdutosAcionados categoria={categoria}/>)}
                        </div>
                    </div> 
                ))}
            </div>
        </div>
    </div>
);
}

export default HomePage;