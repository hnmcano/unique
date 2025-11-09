import axios from "axios";
import React, {useState, useEffect} from "react";

function ProdutosAcionados({categoria}) {
    const [isVisible, setIsVisible] = useState(false);
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const addProduct =  async (categoria, produto) => {

        setLoading(true);
        setError(null);

        const dadosEnviar = {
            cod_sistema: produto.cod_sistema,
            cod_pdv: produto.cod_pdv,
            categoria: categoria.categoria,
            nome: produto.nome,
            preco_custo: produto.preco_custo,
            preco_venda: produto.preco_venda,
            medida: produto.medida,
            estoque: produto.estoque,
            estoque_min: produto.estoque_min,
            sit_estoque: produto.sit_estoque,
            descricao: produto.descricao,
            ficha_tecnica: produto.ficha_tecnica,
            status_venda: produto.status_venda,
            imagem_url: produto.imagem_url,
            quantidade: 1
        };

        console.log('Dados a enviar:',dadosEnviar);

        try {
            const response = await axios.post(`http://127.0.0.1:8000/carrinho/postagem/${produto.cod_sistema}`, dadosEnviar);
            console.log('Resposta do servidor:', response.data);
        } catch (error) {
            console.error('Erro ao enviar os dados:', error);
            setError(error.message);
        } finally {
            setLoading(false);
        }
    }

    const toggleVisibility = () => {
        setIsVisible(!isVisible);
    };

    
    return (
        <div className="products-gouped">
            {categoria.produtos.map((produto) => (
            <div key={produto.cod_sistema} className="produto_item">
                <div className="data-itens-product">
                    <div className="itens-product-img">
                    </div>
                    <div className="data-itens-unique">
                        <div className="data-itens-unique-name">
                            {produto.nome}
                        </div>
                        <div className="data-itens-unique-description">
                            {produto.descricao}
                        </div>
                        <div className="data-itens-unique-select">
                            <div className="data-itens-unique-select-quantity">
                                <button className="buttonquantitymore">+</button>
                                <label className="quantity-number"></label>
                                <button className="buttonquantityless">-</button>
                                <button onClick={() => addProduct(categoria, produto)} className="data-itens-unique-select-adicionar">ADICIONAR</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            ))}
        </div>
    );
}

export default ProdutosAcionados;