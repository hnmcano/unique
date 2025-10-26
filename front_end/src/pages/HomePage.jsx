import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles/HomePage.css"
import ProdutosAcionados from "../components/produtos";

function HomePage(){
    const [base, setBase] = useState(null);
    const [categoriaVisible, setCategoriaVisible] = useState({});
    const [isMenuOpen, setMenuOpen] = useState(true );
    
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
        <div 
        className="button_menu" 
        style={{ marginLeft: isMenuOpen ? '130px' : '20px'
        }}
        >
            <button onClick={toggleMenu} class="menu-icon">☰</button>
        </div>
        <div className={`container_ ${isMenuOpen ? 'open' : 'closed'}`}
                style={{ display: isMenuOpen ? 'block' : 'none'}}>
            <div className="icon_menu">
                <div className="label-menu">
                    <label>Menu Items</label>
                </div>
            </div>
            <div>
                <li className="list_buttons">teste</li>
                <li className="list_buttons" >teste1</li>
            </div>
        </div>
        <div className="container__">
            <div className="logo"></div>
            <div className="produtos">
                    {base && base.map((categoria, index) => (
                        <div key={index}>
                        <div className="categoria" onClick={() => toggleVisibility(index)}>{categoria.categoria}</div>
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