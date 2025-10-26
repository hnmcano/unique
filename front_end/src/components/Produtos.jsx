import React, {useState, useEffect} from "react";

function ProdutosAcionados({categoria}) {
    const [isVisible, setIsVisible] = useState(false);

    const toggleVisibility = () => {
        setIsVisible(!isVisible);
    };
    
    return (
        <div className="produtos_agrupados">
            {categoria.produtos.map((produto) => (
                <div key={produto.cod_sistema} className="produto_item">
                    <div className="produto_disp">
                        <div className="name_product">
                            <div className="nome">{produto.nome}</div>
                        </div>
                        <div className="descricao">{produto.descricao}</div>
                        <div className="preco_venda">{produto.preco_venda}</div>
                    </div>
                </div>
            ))}
        </div>
    );
}

export default ProdutosAcionados;