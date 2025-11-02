import React, { useRef, useEffect, useState } from "react";
import axios from "axios";
import "../styles/Carrinho.css"
import Draggable from "react-draggable";

function ModalShopping({closeModal, openModal, children}){
    const [base, setBase] = useState(null);
    const nodeRef = useRef(null);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/carrinho/carrinho")
            .then(response => {
                setBase(response.data);
                console.log(response.data);
            })
            .catch(error => {
                console.error('Erro ao receber os dados da tabela:', error);
            });
        }, 
    []);

    if (!openModal) return null;

    return (
    <div className="modal-overlay" onClick={closeModal}>
        <Draggable nodeRef={nodeRef} handle=".modal-header-handle" bounds="parent">
            <div ref={nodeRef} className="modal-content" onClick={(e) => e.stopPropagation()}>
                <div className="modal-header-handle">
                    <h3>Arraste o Carrinho</h3>
                </div>
                
                {/* O conteúdo que for passado (ex: seu formulário) */}
                <div className="shoppingcartproductsdivsuperior">
                        <label className="titleproductsshoppingcart">Carrinho de Compras</label>
                        <button className="modal-close-btn" onClick={closeModal}>&times;</button>
                </div>

                {children}

                <div className="listproductsshoppingcart">
                    {base && base.map((cod_sistema) => (
                        <div className="shoppingcartproducts" key={cod_sistema}>
                            <div className="nameproductsshoppingcart">{cod_sistema.nome}</div>
                            <div className=""></div>
                            <div className="valueproductsshoppingcart">
                                <label>R${parseFloat(cod_sistema.preco_venda).toFixed(2)}</label>
                            </div>
                            <div className="modifyproductsshoppingcart">
                                <button className="buttonquantitymore">+</button>
                                <label className="quantity-number">1</label>
                                <button className="buttonquantityless">-</button>
                                <button className="buttondeleteitem">-</button>
                            </div>
                        </div>
                    ))}
                    <div style={{"flex-grow": "1"}}></div>
                </div>
                
                <div className="modal-footer">
                    <div className="totalvalueshoppingcart">
                        <label className="totalvalueshoppingcart">Total: R$ 0,00</label>
                        <label className="totalvalueshoppingcart">Desconto: R$ 0,00</label>
                        <label className="totalvalueshoppingcart">Qtd: 0</label>
                    </div>
                    <button className="buttonfinishbuy">Finalizar Compra</button>
                    <button className="buttonfinishcancel">Excluir</button>
                </div>
            </div>
        </Draggable>
    </div>
  );
}

export default ModalShopping;