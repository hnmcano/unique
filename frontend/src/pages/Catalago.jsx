// importando funções de estado, referencia e efeitos do React

import { useState, useEffect } from "react";

// importando hook de produtos
import { useProdutos } from "../hooks/useProdutos";

// importando hook de estabelecimento
import { useEstabelecimento, statusEstabelecimento } from "../hooks/estabelecimento";


// importando components Menu
import MenuCatalago from "../components/Catalago/MenuCatalago";

// importando componentes da pagina
import ListCategoriasCatalago from "../components/Catalago/ListCategoriasCatalago";
import IconMenuCatalago from "../components/Catalago/IconMenuCatalago";
import DadosLojaCatalago from "../components/Catalago/DadosLojaCatalago";
import LimparFiltroCatalago from "../components/Catalago/LimparFiltroCatalago";
import FiltrosCategCatalogo from "../components/Catalago/FiltrosCategCatalago";

function ContainerCategories() {
    const { base: produtos, isLoading, isFetching, error, refetch } = useProdutos();
    const [estabelecimento, setEstabelecimento ] = useEstabelecimento();
    const [CategoriesLoopList, setCategoriesLoopList] = useState(true);
    const [selectedCategories, setSelectedCategories] = useState(null);
    const [Categories, setCategories] = useState(false);
    const [MenuOpen, setMenuOpen] = useState(false);
    const status = statusEstabelecimento();

    if (isLoading) {
        return (
            <div className="liquid-loader">
                <div className="loading-text">
                    Loading
                    <span className="dot">
                    .
                    </span>
                    <span className="dot">
                    .
                    </span>
                    <span className="dot">
                    .
                    </span>
                </div>
                <div className="loader-track">
                <div className="liquid-fill">
                </div>
            </div>
        </div>
        );
    };
    
    const handleFilterClick = (categoryName) => {
        setSelectedCategories(prevCategory => prevCategory === categoryName ? null : categoryName);
    };

    return (
        <div className="main">
                <IconMenuCatalago MenuOpen={MenuOpen} setMenuOpen={setMenuOpen} setCategories={setCategories} />
            <div className="header">
                <DadosLojaCatalago estabelecimento={estabelecimento} status={status}/>
                <LimparFiltroCatalago setSelectedCategories={setSelectedCategories}/>
                <FiltrosCategCatalogo selectedCategories={selectedCategories} produtos={produtos} handleFilterClick={handleFilterClick}/>
            </div>
            <div className="container_">
                {CategoriesLoopList && <ListCategoriasCatalago selectedCategories={selectedCategories} />}
            </div>
        </div>
    );
}

export default ContainerCategories;




