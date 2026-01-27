import { useCheckout } from "../../contexts/CheckoutContext";
import { Link } from "react-router-dom";

function FormasPagPedido() {
    const { data, setData } = useCheckout();

    const listaPayment = [ 
        {"id": "cc","tipo": "Cartão de Credito"},
        {"id": "cd", "tipo": "Cartão de Debito"}, 
        {"id": "pix", "tipo": "Pix"}, 
        {"id": "din", "tipo": "Dinheiro"}
    ]

    const handledChangeInfos = (event) => {
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            [name]: value,
        }));

    }

    const handledSubmit = async (event) => {
        event.preventDefault();
        const response = await api.post("/pedidos/react", data);
    }

    return (
        <>
            <div className="dropdowns">
                <div className="div-dropdown-payment">
                    <label>Metodo de Pagamento</label>
                    <select name="metodo_pagamento" value={data.metodo_pagamento} onChange={handledChangeInfos} style={{"width": "220px", "margin-top": "10px", "height": "25px", "border-radius": "5px"}}>
                        {listaPayment.map(formas => (
                            <option   key={formas.id} value={formas.id}>{formas.tipo}</option>
                        ))}
                    </select>
                </div>
                <div className="div-dropdown-payment" disabled>
                    <label>Bandeira</label>
                    <select disabled style={{"width": "220px", "margin-top": "10px", "height": "25px", "border-radius": "5px"}}>
                        {listaPayment.map(formas => (
                            <option value={formas.id}>{formas.tipo}</option>
                        ))}
                    </select>
                </div>
                <div className="finalizacao-data">
                    <div className="observacoes">
                        <label style={{"width": "75%"}}>OBSERVAÇÕES</label>
                        <input className="input-observacoes" id="inputObs" type="text" name="observacoes" value={data.observacoes} onChange={handledChangeInfos}></input>
                    </div>
                    <div className="Botoes-Checkout">
                        <button className="continuar-Checkout" onClick={handledSubmit} type="submit">Finalizar Compra</button>
                        <Link to="/">
                            <button className="botao-cancelar-compra" type="button">Continuar Comprando</button>
                        </Link>
                        <Link to="/Checkout/Etapa2">
                            <button className="voltar" type="button">Voltar</button>
                        </Link>
                    </div>
                </div>
            </div>
        </>
    )

}


export default FormasPagPedido;