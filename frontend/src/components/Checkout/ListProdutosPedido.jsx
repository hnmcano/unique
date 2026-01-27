import { useState } from "react";
import { useCheckout } from "../../contexts/CheckoutContext";
import { Link } from "react-router-dom";

function ListProdutosPedido({}){
    const { produtos, totalQuantidade, totalValor } = useCheckout();
    
    return (
        <>
            <div className="data-carrinho">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>NOME</th>
                            <th>QUANTIDADE</th>
                            <th>VALOR TOTAL</th>
                        </tr>
                    </thead>
                    <tbody>
                        {produtos.map(p =>(
                            <tr key={p.produto_id}>
                                <td name="produto_id">{p.produto_id}</td>
                                <td>{p.nome}</td>
                                <td>{p.quantidade}</td>
                                <td className="value-produto"><label>R$</label>{p.valor_total.toFixed(2)}</td>
                            </tr>
                    ))}
                        <tr className="line-foot">
                            <td style={{"textAlign": "left"}} colSpan="2">Total</td>
                            <td style={{"margin": "5px",}}>{totalQuantidade}</td>
                            <td style={{"margin": "5px",}} className="value-produto"><label>R$</label>{totalValor.toFixed(2)}</td>
                        </tr>
                    </tbody>
                </table>
                <div className="Botoes-Checkout">
                    <Link to="/Checkout/Etapa1">
                        <button className="voltar" type="button">Voltar</button>
                    </Link>
                    <Link to="/Checkout/Etapa3">
                        <button className="continuar-Checkout" >Continuar</button>
                    </Link>
                </div>
            </div>
        </>
    )

}


export default ListProdutosPedido;