import { useCheckout } from "../../contexts/CheckoutContext";
import { Link } from "react-router-dom";
import api from "../../api/api";
import { PagamentoCredito, PagamentoDebito, PagamentoDinheiro, PagamentoPix } from "./pagamentos/FormasDePagamentos";
import { IconePix, IconeCredito, IconeDebito, IconeDinheiro } from "./pagamentos/iconesSvg";
import { useState } from "react";

function FormasPagPedido() {
    const { data, 
            setData, 
            valor_total, 
            ToogleVisibility, 
            opcoesDisponiveis,
            formaPagamento,
            handleSelect
        } = useCheckout();


    const handledSubmit = async (event) => {
        
        event.preventDefault();

        const response = await api.post("/pedidos/react", data);
        const pedido = response.data;
        console.log(pedido);
    }
    
    return (
        <>
        <div className="metodos-pagamento-container">
            <div className="formas-pagamentos">
                <div className="opcao-pagamento" >
                    <label className="checkbox-pagamentos" onClick={() => ToogleVisibility("pix")} >
                        <IconePix onClick={() => ToogleVisibility("pix")}/>
                        <span className="label-checkbox-pagamentos" onClick={() => ToogleVisibility("pix")}>PIX</span>
                        <input
                            type="radio"
                            name="pagamento"
                            value="pix"
                            style={{ display: "none"}}
                            checked={formaPagamento === "pix"}
                            onChange={() => handleSelect("pix")}
                        />
                    </label>
                    {opcoesDisponiveis === "pix" && (<PagamentoPix />)}
                </div>
               <div className="opcao-pagamento" >
                    <label className="checkbox-pagamentos" onClick={() => ToogleVisibility("credito")}>
                        <IconeCredito onClick={() => ToogleVisibility("credito")}/>
                        <span className="label-checkbox-pagamentos" onClick={() => ToogleVisibility("credito")}>CRÉDITO</span>
                        <input
                            type="radio"
                            name="pagamento"
                            value="credito"
                            style={{ display: "none"}}
                            checked={formaPagamento === "credito"}
                            onChange={() => handleSelect("credito")}
                        />
                    </label>
                    {opcoesDisponiveis === "credito" && (<PagamentoCredito />)}
                </div>
                <div className="opcao-pagamento" >
                    <label className="checkbox-pagamentos" onClick={() => ToogleVisibility("debito")}>
                        <IconeDebito onClick={() => ToogleVisibility("debito")} />
                        <span className="label-checkbox-pagamentos" onClick={() => ToogleVisibility("debito")}>DÉBITO</span>
                        <input
                            type="radio"
                            name="pagamento"
                            value="debito"
                            style={{ display: "none"}}
                            checked={formaPagamento === "debito"}
                            onChange={() => handleSelect("debito")}
                        />
                    </label>
                    {opcoesDisponiveis === "debito" && (<PagamentoDebito />)}
                </div>
                <div className="opcao-pagamento" >
                    <div className="checkbox-pagamentos" onClick={() => ToogleVisibility("dinheiro")}>
                        <IconeDinheiro onClick={() => ToogleVisibility("dinheiro")}/>
                        <span className="label-checkbox-pagamentos" onClick={() => ToogleVisibility("dinheiro")}>DINHEIRO</span>
                        <input
                            type="radio"
                            name="pagamento"
                            value="dinheiro"
                            style={{ display: "none"}}
                            checked={formaPagamento === "dinheiro"}
                            onChange={() => handleSelect("dinheiro")}
                        />
                    </div>
                    {opcoesDisponiveis === "dinheiro" && (<PagamentoDinheiro />)}
                </div>
            </div>
            <div style={{"width":"100%"}}>
                <div className="container-total-geral" style={{marginBottom: "20px"}}>
                    <h3 style={{"color": "white"}}>TOTAL GERAL</h3>
                    <h3 className="value-total-geral"><label>R$</label>{valor_total.toFixed(2)}</h3>
                </div>
                <div className="Botoes-Checkout">
                    <Link to="/Checkout/Etapa2">
                        <button className="voltar" type="button">VOLTAR</button>
                    </Link>
                    <button onClick={handledSubmit} className="continuar-Checkout" type="submit">FINALIZAR COMPRA</button>
                </div>
            </div>
        </div>
        </>
    )

}


export default FormasPagPedido;