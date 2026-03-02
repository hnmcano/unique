import { Link } from "react-router-dom";

function BotaoFinalizacao({closeModal}) {
    return (
        <>
        {/* Botão para finalizar compra */}
        <div className="finish-conclusion">
            <Link to="/Checkout/Etapa1">
                <button onClick={closeModal}  className="pushable">
                    <span className="shadow"></span>
                    <span className="edge"></span>
                    <span className="front"> Finalizar Pedido </span>
                </button>
            </Link>
            {/* Botão para excluir carrinho */}
            {/*<button onClick={() => delCartShopping()} className="button-finish-cancel" disabled={isLoading}>Excluir Carrinho</button>*/}
        </div>

        </>
    );

};


export default BotaoFinalizacao;