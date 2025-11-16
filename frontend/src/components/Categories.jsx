import { useEffect, useState } from "react";
import { useProdutos } from "../hooks/useProdutos";
import ProdutosAcionados from "./Produtos";

function CategoriesLoop({selectedCategories}) {
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

    const filteredCategories = selectedCategories ? setBaseProdutos.filter(categoria => categoria.categoria === selectedCategories) : setBaseProdutos;

    return (
        <div>
            {filteredCategories && filteredCategories.map((categoria) => (
                <div key={categoria.categoria}>
                <div className="categories-details" onClick={() => toggleVisibility(categoria.categoria)}>{categoria.categoria}</div>
                    <div>
                        {categoriaVisible[categoria.categoria] && ( <ProdutosAcionados categoria={categoria}/>)}
                    </div>
                </div> 
            ))}
        </div>
    )
};


export default CategoriesLoop;
