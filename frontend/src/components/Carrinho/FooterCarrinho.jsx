import BotaoFinalizacao from "./BotaoFinalizarCarrinho";
import { useCarrinho } from "../../hooks/useCarrinho";
import React, { useState, useEffect } from "react";

function FooterCarinho({closeModal, openModal}) {
    const { produtos, quantidadeItems } =  useCarrinho();
    const [total, setTotal] = useState(0);

    //Calcular o total
    useEffect(() => {
        // se o modal for aberto, calcular o total
        if(openModal){
            // Realiza um mapeamento dos produtos no carrinho, e soma o preco_venda * quantidade
            // De acordo com que as dependencias tenham modificações
            const soma = produtos.reduce((acc, p) => acc + (p.preco_venda * p.quantidade), 0);
            // Altera o estado do total
            setTotal(soma);
        }
        // Dependencias, baseadas nos produtos e se o modal estiver aberto, para calcular o total
    }, [produtos, openModal]);


    return (
        <>
            {/* Rodapé do modal */}
            <div className="modal-footer">
                {/* O total por valores e quantidade de produtos unicos */}
                <div className="total-values-shopping-cart">
                    {/* label para o total por valor */}
                    <div>
                        <label className="total-value-shopping-cart-total">Total: R$ {total.toFixed(2)}</label>
                    </div>
                    {/* label para a quantidade de produtos no carrinho (unicos) */}
                    <div>
                        <label className="total-values-shopping-cart-qtd">Qtd: {quantidadeItems}</label>
                    </div>
                </div>
                {/* Botão para finalizar compra */}
                <BotaoFinalizacao 
                    closeModal={closeModal}
                />
            </div>
        </>
    );

}

export default FooterCarinho;