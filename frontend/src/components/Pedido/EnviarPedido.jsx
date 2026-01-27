import { Link } from "react-router-dom";
import Carrinho from "../../pages/Carrinho";


function EnviarPedido({handledSubmit, openModal, modalShoppingOpen, closeModal, data,  handledChangeInfos }) {

    return (
        <>
            <div className="finalizacao-data">
                <div className="observacoes">
                    <label style={{"width": "75%"}}>OBSERVAÇÕES</label>
                    <input className="input-observacoes" id="inputObs" type="text" name="observacoes" value={data.observacoes} onChange={handledChangeInfos}></input>
                </div>
                <div className="botoes-finalizacao">
                    <button onClick={handledSubmit} className="botao-finalizar-compra" type="submit">Finalizar Compra</button>
                    <Link to="/">
                        <button className="botao-cancelar-compra" type="button">Continuar Comprando</button>
                    </Link>

                    <button onClick={openModal} className="botao-cancelar-compra" type="button"><Carrinho  openModal={modalShoppingOpen} closeModal={closeModal}></Carrinho>Editar Carrinho</button>
                    <button className="botao-cancelar-compra" type="button">Limpar Dados</button>
                </div>
            </div>
        </>
    )
}


export default EnviarPedido;