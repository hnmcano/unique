// importando a função de estado do react 
import ContainerCategories from "./Catalago";
//import Options from "../components/Options";
import { useState } from "react";
import "../styles/Inicio.css"

// Função da pagina principal
function HomePage(){
    const [Categories, setCategories] = useState(true);
    
    return (
    <div className="home">
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