import { useState } from "react";
import { useProdutos } from "../hooks/useProdutos";
import CategoriesLoop from "./Categories";

function ContainerCategories() {
    const { base: setBaseProdutos } = useProdutos();
    const [CategoriesLoopList, setCategoriesLoopList] = useState(true);
    const [selectedCategories, setSelectedCategories] = useState(null);

    const handleFilterClick = (categoryName) => {
        setSelectedCategories(prevCategory => prevCategory === categoryName ? null : categoryName);
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
                <div className="filter-all">
                    <button onClick={() => setSelectedCategories(null)} className="button-filter">Limpar filtro</button>
                </div>
                <div className="buttons-filters">
                    {setBaseProdutos && setBaseProdutos.map((categoria, index) => (
                        <button onClick={() => handleFilterClick(categoria.nome_categoria)} className={`buttons-filters ${selectedCategories === categoria.nome_categoria ? 'active' : ''}`}>{categoria.nome_categoria}</button>
                    ))}
                </div>
            </div>

            <div className="container_">
                {CategoriesLoopList && <CategoriesLoop selectedCategories={selectedCategories} />}
            </div>
        </div>
    );
}

export default ContainerCategories;




