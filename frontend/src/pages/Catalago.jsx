// importando funções de estado, referencia e efeitos do React

import React, { useState, useEffect } from "react";

// importando hook de produtos
import { useProdutos } from "../hooks/useProdutos";

// importando hook de estabelecimento
import { useEstabelecimento } from "../contexts/EstabelecimentoContext";
import { useCarrinho } from "../contexts/CarrinhoContext";

// importando componentes da pagina
import ListCategoriasCatalago from "../components/Catalago/ListCategoriasCatalago";
import IconMenuCatalago from "../components/Catalago/IconMenuCatalago";
import DadosLojaCatalago from "../components/Catalago/DadosLojaCatalago";
import LimparFiltroCatalago from "../components/Catalago/LimparFiltroCatalago";
import FiltrosCategCatalogo from "../components/Catalago/FiltrosCategCatalago";
import FooterCatalago from "../components/Catalago/FooterCatalago";
import BotaoCarrinho from "../components/Carrinho/BotaoCarrinho";

function ContainerCategories() {
    const { base, isLoading, isFetching, error, refetch } = useProdutos();
    const { produtos } = useCarrinho();
    const { estabelecimento }= useEstabelecimento();
    const [CategoriesLoopList, setCategoriesLoopList] = useState(true);
    const [selectedCategories, setSelectedCategories] = useState(null);
    const [modalOpenProduto, setModalOpenProduto] = useState(false);
    const [botao, setBotao] = useState(false);
    const [Categories, setCategories] = useState(false);
    const [MenuOpen, setMenuOpen] = useState(false);

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
                    <div className="liquid-fill"></div>
                </div>
            </div>
        );
    };
    
    const handleFilterClick = (categoryName) => {
        setSelectedCategories(prevCategory => prevCategory === categoryName ? null : categoryName);
    };
    

    return (
        <>
            <div className="header">
                <IconMenuCatalago MenuOpen={MenuOpen} setMenuOpen={setMenuOpen} setCategories={setCategories} />
                <DadosLojaCatalago estabelecimento={estabelecimento}/>
                <LimparFiltroCatalago setSelectedCategories={setSelectedCategories}/>
                <FiltrosCategCatalogo selectedCategories={selectedCategories} produtos={base} handleFilterClick={handleFilterClick}/>
            </div>
            <div className="produtos-catalago">
                {CategoriesLoopList && <ListCategoriasCatalago selectedCategories={selectedCategories} />}
            </div>
            <div className="footer-catalago">
                <FooterCatalago/>
            </div>
            {produtos.length > 0 && 
                <BotaoCarrinho MenuOpen={MenuOpen} quantidade={produtos.length} setModalOpenProduto={setModalOpenProduto}/>
            }
        </>
    );
}

export default ContainerCategories;




