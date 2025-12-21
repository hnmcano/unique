import { CiBoxList } from "react-icons/ci";
import { GiShoppingCart } from "react-icons/gi";
import { FaRegUserCircle } from "react-icons/fa";
import ModalShopping from "./Carrinho";

function Options() {
    // Estabelecendo estado do modal carrinho como falso, ou seja fechado, para ser aberto quando o botão de carrinho for clicado.

    // Funções para abrir e fechar o modal carrinho


    return (
        <div className="icons-ajustes">
            <div className="icons-options">
                <CiBoxList className="icons" />
            </div>
            <div className="icons-options">
                <GiShoppingCart className="icons" />
                <ModalShopping></ModalShopping>
            </div>
            <div className="icons-options">
                <FaRegUserCircle className="icons" />
            </div>
        </div>
    );
}


export default Options;