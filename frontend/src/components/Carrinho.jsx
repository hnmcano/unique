import React, { useRef, useState, useEffect, use} from "react";
import axios from "axios";
import "../styles/Carrinho.css"
import Draggable from "react-draggable";
import { removerProduto } from "../api/carrinhoServices";
import { useCarrinho } from "../hooks/useCarrinho";


function ModalShopping({closeModal, openModal, children}){
    const [total, setTotal] = useState(0);
    const [carrinho, setCarrinho] = useState([]);
    const { produtos, setProdutos } = useCarrinho();
    const nodeRef = useRef(null);

    //Somar o total por produtos
    const handleQuantidade = (id, delta) => {
        setProdutos(prev => 
            prev.map(p => 
                p.cod_sistema === id 
                ? {...p, quantidade: Math.max(1, p.quantidade + delta) } : p
            )
        );
    }
    //Calcular o total
    useEffect(() => {
        const soma = produtos.reduce((acc, p) => acc + (p.preco_venda * p.quantidade), 0);
        setTotal(soma);    
    }, [produtos]);


    const handleRemover = async (cod_sistema) => {
        try {
            await removerProduto(cod_sistema);
            setProdutos(prev => prev.filter(p => p.cod_sistema !== cod_sistema));
        } catch (error) {
            console.error('Erro ao remover:', error);
        }
    };


    if (!openModal) return null;

    return (
    <div className="modal-overlay" onClick={closeModal}>
        <Draggable nodeRef={nodeRef} handle=".modal-header-handle" bounds="parent">
            <div ref={nodeRef} className="modal-content" onClick={(e) => e.stopPropagation()}>
                
                <div className="modal-header-handle">
                    <label className="titleproductsshoppingcart">Carrinho de Compras</label>
                    <button className="modal-close-btn" onClick={closeModal}>&times;</button> 
                </div>
                
                {/* O conteúdo que for passado (ex: seu formulário) */}
                {children}

                <div className="listproductsshoppingcart">
                    {produtos.map((p) => (
                    <div className="shoppingcartproducts" key={p.cod_sistema}>
                        <div className="nameproductsshoppingcart">{p.nome}</div>
                        <div className=""></div>
                        <div className="valueproductsshoppingcart">
                        <label>R${(p.preco_venda * p.quantidade).toFixed(2)}</label>
                        </div>
                        <div className="modifyproductsshoppingcart">
                        <button onClick={() => handleQuantidade(p.cod_sistema, 1)} className="buttonquantitymore">+</button>
                        <label className="quantity-number">{p.quantidade}</label>
                        <button onClick={() => handleQuantidade(p.cod_sistema, -1)} className="buttonquantityless">-</button>
                        <button onClick={() => handleRemover(p.cod_sistema)} className="buttondeleteitem">-</button>
                        </div>
                    </div>
                    ))}
                    <div style={{"flex-grow": "1"}}></div>
                </div>
                
                <div className="modal-footer">
                    <div className="totalvalueshoppingcart">
                        <label className="totalvalueshoppingcart">Total: R$ {total.toFixed(2)}</label>
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