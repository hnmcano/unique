import ProdutosAcionados from "./Produtos";
import React, { useState } from "react";
import { useProdutos } from "../hooks/useProdutos";

function ContainerCategories() {
    const { base: setBaseProdutos } = useProdutos();
    const [categoriaVisible, setCategoriaVisible] = useState({});

    const toggleVisibility = (index) => {
        // Converte o índice para string, se necessário, para ser uma chave de objeto consistente
        const indexString = String(index); 
        
        setCategoriaVisible((prevState) => ({
            ...prevState,
            // Usa o índice como chave no estado
            [indexString]: !prevState[indexString],
        }));
    };

    return (
        <div>
            {setBaseProdutos && setBaseProdutos.map((categoria, index) => (
                <div key={index}>
                <div className="categories-details" onClick={() => toggleVisibility(index)}>{categoria.categoria}</div>
                    <div>
                        {categoriaVisible[String(index)] && ( <ProdutosAcionados categoria={categoria}/>)}
                    </div>
                </div> 
            ))}
        </div>
    );
}

export default ContainerCategories;




