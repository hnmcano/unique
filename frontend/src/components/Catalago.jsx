import { useState } from "react";
import { useProdutos } from "../hooks/useProdutos";
import CategoriesLoop from "./Categories";
import { useEstabelecimento } from "../hooks/estabelecimento";

function ContainerCategories() {
    const { base: produtos, isLoading, isFetching, error, refetch } = useProdutos();
    const [estabelecimento, setEstabelecimento ] = useEstabelecimento();
    const [CategoriesLoopList, setCategoriesLoopList] = useState(true);
    const [selectedCategories, setSelectedCategories] = useState(null);

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
        <div>
            <div className="header">
                <div className="logotipo-hookah">
                    <img className="logotipo" src={`data:image/png;base64,${estabelecimento?.logo_base64}`} alt="Logo"/>
                </div>
                <div className="data">
                    <div className="status-container">
                        <label className="status">ABERTO</label>
                    </div>
                    <div className="infos">
                        <div className="infos-data">
                            <div className="montserrat-data">Endereço: {estabelecimento?.endereco}</div>
                        </div>
                        <div className="infos-data">
                            <div className="montserrat-data">Telefone: {estabelecimento?.telefone} | Instagram: {estabelecimento?.instagram}</div>
                        </div>
                        <div className="infos-data">
                            <div className="montserrat-data"> Horário: 13:00 às 17:00</div>
                        </div>
                    </div>
                </div>
                <div className="filter-all">
                    <button onClick={() => setSelectedCategories(null)} className="button-filter"> 
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="16"
                            height="16"
                            fill="currentColor"
                            className="bi bi-arrow-repeat"
                            viewBox="0 0 16 16"
                        >
                        <path 
                        d="M11.534 7h3.932a.25.25 0 0 1 .192.41l-1.966 2.36a.25.25 0 0 1-.384 0l-1.966-2.36a.25.25 0 0 1 .192-.41zm-11 2h3.932a.25.25 0 0 0 .192-.41L2.692 6.23a.25.25 0 0 0-.384 0L.342 8.59A.25.25 0 0 0 .534 9z">
                        </path>
                        <path
                        fillRule="evenodd"
                        d="M8 3c-1.552 0-2.94.707-3.857 1.818a.5.5 0 1 1-.771-.636A6.002 6.002 0 0 1 13.917 7H12.9A5.002 5.002 0 0 0 8 3zM3.1 9a5.002 5.002 0 0 0 8.757 2.182.5.5 0 1 1 .771.636A6.002 6.002 0 0 1 2.083 9H3.1z"
                        >
                        </path>
                        </svg>
                            Limpar Filtros
                        </button>
                </div>
                <div className="div-buttons-filters">
                    {produtos.map((categoria, index) => (
                        <button key={categoria.id || categoria.nome_categoria} 
                            onClick={() => handleFilterClick(categoria.nome_categoria)} 
                            className={`buttons-filters ${
                            selectedCategories === categoria.nome_categoria ? 'active' : ''}`}>
                                {categoria.nome_categoria}
                        </button>
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




