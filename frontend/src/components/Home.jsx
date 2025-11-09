import ProdutosAcionados from "./Produtos";
import { useState } from "react";
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
            <div className="header">
                <div className="logotipo-hookah">
                    <img src="/src/assets/logo_hookahshisha.png" alt="Logo" className="logo"/>
                </div>
                <div className="data">
                    <div className="status-container">
                        <label className="status">ABERTO</label>
                    </div>
                    <div className="infos">
                        <div className="infos-data">
                            <div className="endereço">
                                <div>Endereço: Rua joão constante Carrara, 298</div>
                            </div>
                        </div>
                        <div className="infos-data">
                            <div className="telefone">
                                <label>Telefone: (11) 99999-9999 | Instagram: @hookahshisha</label>
                            </div>
                        </div>
                        <div className="infos-data">
                            <label> Horário: 13:00 às 17:00</label>
                        </div>
                    </div>
                </div>
                
                <div className="buttons-filters">
                    {setBaseProdutos && setBaseProdutos.map((categoria, index) => (
                        <button className="buttons-filters">{categoria.categoria}</button>
                    ))}
                </div>
            </div>
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




