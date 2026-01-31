import { useCheckout } from "../../contexts/CheckoutContext";
import { Link } from "react-router-dom";
import { useState } from "react";

function FormasPagPedido() {
    const { data, setData, valorTotal, ToogleVisibility, opcoesDisponiveis} = useCheckout();

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
        <div className="metodos-pagamento-container">
            <div className="formas-pagamentos">
                <div className="checkbox-pagamentos" onClick={() => ToogleVisibility("pix")}>
                    <label>
                        <svg fill="#14e121" 
                            viewBox="0 0 16 16"
                            height="36" 
                            width="50"
                            xmlns="http://www.w3.org/2000/svg">
                            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                            <g id="SVGRepo_tracerCarrier" 
                                stroke-linecap="round" 
                                stroke-linejoin="round">
                            </g>
                                <g id="SVGRepo_iconCarrier">
                                    <path d="M11.917 11.71a2.046 2.046 0 
                                    0 1-1.454-.602l-2.1-2.1a.4.4 0 0 0-.551 
                                    0l-2.108 2.108a2.044 2.044 0 0 1-1.454.602h-.414l2.66 
                                    2.66c.83.83 2.177.83 3.007 0l2.667-2.668h-.253zM4.25 
                                    4.282c.55 0 1.066.214 1.454.602l2.108 2.108a.39.39 0 0 0 
                                    .552 0l2.1-2.1a2.044 2.044 0 0 1 1.453-.602h.253L9.503 
                                    1.623a2.127 2.127 0 0 0-3.007 0l-2.66 2.66h.414z">
                                    </path>
                                    <path d="m14.377 
                                    6.496-1.612-1.612a.307.307 0 0 
                                    1-.114.023h-.733c-.379 0-.75.154-1.017.422l-2.1 
                                    2.1a1.005 1.005 0 0 1-1.425 0L5.268 5.32a1.448 1.448 0 
                                    0 0-1.018-.422h-.9a.306.306 0 0 1-.109-.021L1.623 
                                    6.496c-.83.83-.83 2.177 0 3.008l1.618 1.618a.305.305 0 
                                    0 1 .108-.022h.901c.38 0 .75-.153 1.018-.421L7.375 8.57a1.034 
                                    1.034 0 0 1 1.426 0l2.1 2.1c.267.268.638.421 1.017.421h.733c.04 
                                    0 .079.01.114.024l1.612-1.612c.83-.83.83-2.178 0-3.008z">
                                    </path>
                                </g>
                        </svg>
                    </label>
                    <label className="label-checkbox-pagamentos">PIX</label>
                    <div>
                        {opcoesDisponiveis["pix"] ? "Visível" : "Oculto"}
                    </div>
                </div>
                <div className="checkbox-pagamentos" onClick={() => ToogleVisibility("credito")}>
                    <label>
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="50px" height="36px" viewBox="0 0 58 40" version="1.1">
                        <title>048 - Add Payment Card</title>
                        <desc>Created with Sketch.</desc>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="048---Add-Payment-Card">
                        <path d="M41.52,36 L4,36 C1.790861,36 2.22044605e-16,34.209139 0,32 L0,4 C-2.22044605e-16,1.790861 1.790861,0 4,0 L50,0 C52.209139,0 54,1.790861 54,4 L54,23.52 L41.52,36 Z" id="Path" fill="#F29C1F"></path>
                        <rect id="Rectangle" fill="#464F5D" x="0" y="6" width="54" height="8"></rect>
                        <path d="M7,25 L5,25 C4.44771525,25 4,24.5522847 4,24 C4,23.4477153 4.44771525,23 5,23 L7,23 C7.55228475,23 8,23.4477153 8,24 C8,24.5522847 7.55228475,25 7,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M13,25 L11,25 C10.4477153,25 10,24.5522847 10,24 C10,23.4477153 10.4477153,23 11,23 L13,23 C13.5522847,23 14,23.4477153 14,24 C14,24.5522847 13.5522847,25 13,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M19,25 L17,25 C16.4477153,25 16,24.5522847 16,24 C16,23.4477153 16.4477153,23 17,23 L19,23 C19.5522847,23 20,23.4477153 20,24 C20,24.5522847 19.5522847,25 19,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M25,25 L23,25 C22.4477153,25 22,24.5522847 22,24 C22,23.4477153 22.4477153,23 23,23 L25,23 C25.5522847,23 26,23.4477153 26,24 C26,24.5522847 25.5522847,25 25,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M58,31 C58.003238,35.1324722 55.1939289,38.7369928 51.1857912,39.7430592 C47.1776536,40.7491256 42.9990957,38.8986012 41.0503577,35.2544611 C39.1016197,31.610321 39.8827089,27.107579 42.9449534,24.3326924 C46.0071979,21.5578058 50.5648867,21.2227553 54,23.52 C56.4983677,25.1892918 57.9988932,27.9952745 58,31 Z" id="Path" fill="#24AE5F"></path>
                        <path d="M53,30 L50,30 L50,27 C50,26.4477153 49.5522847,26 49,26 C48.4477153,26 48,26.4477153 48,27 L48,30 L45,30 C44.4477153,30 44,30.4477153 44,31 C44,31.5522847 44.4477153,32 45,32 L48,32 L48,35 C48,35.5522847 48.4477153,36 49,36 C49.5522847,36 50,35.5522847 50,35 L50,32 L53,32 C53.5522847,32 54,31.5522847 54,31 C54,30.4477153 53.5522847,30 53,30 Z" id="Path" fill="#FFFFFF"></path>
                                </g>
                            </g>
                        </svg>
                    </label>
                    <label className="label-checkbox-pagamentos">CRÉDITO</label>
                    <div>
                        {opcoesDisponiveis["credito"] ? "Visível" : "Oculto"}
                    </div>
                </div>
                <div className="checkbox-pagamentos" onClick={() => ToogleVisibility("debito")}>
                    <label>
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="50px" height="36px" viewBox="0 0 58 40" version="1.1">
                        <title>048 - Add Payment Card</title>
                        <desc>Created with Sketch.</desc>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                        <g id="048---Add-Payment-Card">
                        <path d="M41.52,36 L4,36 C1.790861,36 2.22044605e-16,34.209139 0,32 L0,4 C-2.22044605e-16,1.790861 1.790861,0 4,0 L50,0 C52.209139,0 54,1.790861 54,4 L54,23.52 L41.52,36 Z" id="Path" fill="#F29C1F"></path>
                        <rect id="Rectangle" fill="#464F5D" x="0" y="6" width="54" height="8"></rect>
                        <path d="M7,25 L5,25 C4.44771525,25 4,24.5522847 4,24 C4,23.4477153 4.44771525,23 5,23 L7,23 C7.55228475,23 8,23.4477153 8,24 C8,24.5522847 7.55228475,25 7,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M13,25 L11,25 C10.4477153,25 10,24.5522847 10,24 C10,23.4477153 10.4477153,23 11,23 L13,23 C13.5522847,23 14,23.4477153 14,24 C14,24.5522847 13.5522847,25 13,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M19,25 L17,25 C16.4477153,25 16,24.5522847 16,24 C16,23.4477153 16.4477153,23 17,23 L19,23 C19.5522847,23 20,23.4477153 20,24 C20,24.5522847 19.5522847,25 19,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M25,25 L23,25 C22.4477153,25 22,24.5522847 22,24 C22,23.4477153 22.4477153,23 23,23 L25,23 C25.5522847,23 26,23.4477153 26,24 C26,24.5522847 25.5522847,25 25,25 Z" id="Path" fill="#F3D55B"></path>
                        <path d="M58,31 C58.003238,35.1324722 55.1939289,38.7369928 51.1857912,39.7430592 C47.1776536,40.7491256 42.9990957,38.8986012 41.0503577,35.2544611 C39.1016197,31.610321 39.8827089,27.107579 42.9449534,24.3326924 C46.0071979,21.5578058 50.5648867,21.2227553 54,23.52 C56.4983677,25.1892918 57.9988932,27.9952745 58,31 Z" id="Path" fill="#24AE5F"></path>
                        <path d="M53,30 L50,30 L50,27 C50,26.4477153 49.5522847,26 49,26 C48.4477153,26 48,26.4477153 48,27 L48,30 L45,30 C44.4477153,30 44,30.4477153 44,31 C44,31.5522847 44.4477153,32 45,32 L48,32 L48,35 C48,35.5522847 48.4477153,36 49,36 C49.5522847,36 50,35.5522847 50,35 L50,32 L53,32 C53.5522847,32 54,31.5522847 54,31 C54,30.4477153 53.5522847,30 53,30 Z" id="Path" fill="#FFFFFF"></path>
                                </g>
                            </g>
                        </svg>
                    </label>
                    <label className="label-checkbox-pagamentos">DÉBITO</label>
                    <div>
                        {opcoesDisponiveis["debito"] ? "Visível" : "Oculto"}
                    </div>
                </div>
            </div>
            <div style={{"width":"100%"}}>
                <div className="container-total-geral" style={{marginBottom: "20px"}}>
                    <h3 style={{"color": "white"}}>TOTAL GERAL</h3>
                    <h3 className="value-total-geral"><label>R$</label>{valorTotal.toFixed(2)}</h3>
                </div>
                <div className="Botoes-Checkout">
                    <Link to="/Checkout/Etapa2">
                        <button className="voltar" type="button">VOLTAR</button>
                    </Link>
                    <button className="continuar-Checkout" type="submit">CONTINUAR</button>
                </div>
            </div>
        </div>
        </>
    )

}


export default FormasPagPedido;