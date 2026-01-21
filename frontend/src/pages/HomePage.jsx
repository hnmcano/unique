// importando a função de estado do react 
import ContainerCategories from "../components/Catalago";
//import Options from "../components/Options";
import { useEffect, useState } from "react";
import "../styles/HomePage.css"
import Options from "../components/Options";

// Função da pagina principal
function HomePage(){
    const [Categories, setCategories] = useState(true);
    const [MenuOpen, setMenuOpen] = useState(false);

    return (
    <div className="home">
        <button className={`menuButton ${MenuOpen ? "active" : ""}`} 
        onClick={() => setMenuOpen(prev => !prev)}
        aria-expanded={MenuOpen}
        >
            <span className="top"/>
            <span className="mid"/>
            <span className="bot"/>
        </button>
        <div className="Menu">
            {MenuOpen && <Options 
            MenuOpen={MenuOpen} 
            setMenuOpen={setMenuOpen} 
            setCategories={setCategories}/>}
        </div>
        <div className="container">
            {/* Condicional para exibir o componente Home ou finalização de acordo com o botão clicado */}
            {/* Componente Home: /components/Home */}
            {Categories && <ContainerCategories/>}
            {/* Componente Finalizacao: /components/Finalizacao */}
        </div>
    </div>
);
}

// Exportando a função HomePage como padrão.
export default HomePage;