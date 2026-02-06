import { useState } from "react";
import { useCheckout } from "../../contexts/CheckoutContext";
import { Link, useNavigate } from "react-router-dom";

function ListProdutosPedido({}){
    const { produtos, totalQuantidade, totalValor, valor_total, entregaTaxa } = useCheckout();
    const [checked, setChecked] = useState(false);    
    const navigate = useNavigate();

    const handlesubmit = (e) => {
        e.preventDefault();

        if (checked) {
            navigate("/Checkout/Etapa3");
        }else{
            alert("Por favor, concorde com os termos para continuar.");
            return;
        }
    }

    return (
        <>
            <div className="produtos-pedido-container">
                <div className="tabela-produtos-container">
                    <table className="tabela-produtos">
                            <thead>
                                <tr>
                                    <th>PRODUTO</th>
                                    <th>QTD</th>
                                    <th>VALOR</th>
                                </tr>
                            </thead>
                            <tbody>
                                {produtos.map(p =>(
                                    <tr key={p.produto_id}>
                                        <td>{p.nome}</td>
                                        <td>{p.quantidade}</td>
                                        <td className="value-produto"><label>R$</label>{p.valor_total.toFixed(2)}</td>
                                    </tr>
                            ))}
                                <tr className="line-foot">
                                    <td style={{"textAlign": "left"}} colSpan="1">Total</td>
                                    <td style={{"margin": "5px",}}>{totalQuantidade}</td>
                                    
                                    <td style={{"margin": "5px",}} className="value-produto"><label>R$</label>{totalValor.toFixed(2)}</td>
                                </tr>
                            </tbody>
                    </table>
                </div>
                <div>
                    <table className="tabela-produtos">
                        <thead>
                            <tr>
                                <th> VALOR ENTREGA</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style={{"padding": "10px", "display": "flex","justifyContent": "space-between"}}><label>R$</label>{entregaTaxa.toFixed(2)}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div>
                    <div className="container-total-geral">
                        <h3 style={{"color": "white"}}>TOTAL GERAL</h3>
                        <h3 className="value-total-geral"><label>R$</label>{valor_total.toFixed(2)}</h3>
                    </div>
                    <div className="checkbox-wrapper-33">
                        <label className="checkbox">
                            <input className="checkbox__trigger visuallyhidden" 
                            type="checkbox"
                            checked={checked}
                            onChange={(e) => setChecked(e.target.checked)} />
                            <span className="checkbox__symbol">
                            <svg
                                aria-hidden="true"
                                className="icon-checkbox"

                                width="28px"
                                height="28px"
                                viewBox="0 0 28 28"
                                version="1"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path d="M4 14l8 7L24 7"></path>
                            </svg>
                            </span>
                            <p className="checkbox__textwrapper">Ao continuar, voce concorda com os dados do pedido descrito na tabela acima e o valor total.</p>
                        </label>
                    </div>
                    <div className="Botoes-Checkout">
                        <Link to="/Checkout/Etapa1">
                            <button className="voltar" type="button">VOLTAR</button>
                        </Link>
                        <button onClick={handlesubmit} type="submit" disabled={!checked} className={!checked ? "disabled-continuar-checkout" : "continuar-Checkout"}>CONTINUAR</button>
                    </div>
                </div>
            </div>
        </>
    )

}


export default ListProdutosPedido;