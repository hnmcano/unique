import axios from "axios";
import React, {useState, useEffect} from "react";

function ProdutosAcionados({categoria}) {
    const [isVisible, setIsVisible] = useState(false);
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)
    const [imagem, setImagem] = useState("");

    const addProduct =  async (categoria, produtos) => {

        console.log(produtos);

        setLoading(true);
        setError(null);

        const dadosEnviar = {
            produto_id: produtos.produto_id,
            cod_pdv: produtos.cod_pdv,
            nome: produtos.nome,
            categoria: categoria.nome_categoria,
            preco_custo: produtos.preco_custo,
            preco_venda: produtos.preco_venda,
            medida: produtos.medida,
            estoque: produtos.estoque,
            estoque_min: produtos.estoque_min,
            sit_estoque: produtos.sit_estoque,
            descricao: produtos.descricao,
            ficha_tecnica: produtos.ficha_tecnica,
            status_venda: produtos.status_venda,
            imagem_url: produtos.imagem_url,
            quantidade: 1
        };

        console.log('Dados a enviar:',dadosEnviar);

        try {
            const response = await axios.post(`http://127.0.0.1:8000/carrinho/adicionar-produto/${produtos.produto_id}`, dadosEnviar);
            console.log('Resposta do servidor:', response.data);
        } catch (error) {
            console.error('Erro ao enviar os dados:', error);
            setError(error.message);
            console.error('Erro ao enviar os dados:', dadosEnviar);
        } finally {
            setLoading(false);
        }
    }


    const toggleVisibility = () => {
        setIsVisible(!isVisible);
    };

    const imagemUrl = (imagem) => `data:image/png;base64,${imagem}`;
    
    return (    
        <div className="products-gouped">
            {categoria.produtos.map((produtos) => (
            <div key={produtos.produto_id} className="produtos-item">
                <div className="data-itens-product">
                    <div className="data-img-container">
                        <img className="img-product" src={imagemUrl(produtos.imagem)} alt="imagem produto"/>
                    </div>
                    <div className="data-description-container">
                        <div>
                            {produtos.nome}
                        </div>
                        <div className="data-description">
                            {produtos.descricao}
                        </div>
                        <div>
                            <div className="data-adicionar-container">
                                <button onClick={() => addProduct(categoria, produtos)} className="cart-button">
                                    <svg className="cart-icon" stroke="currentColor" strokeWidth="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" strokeLinejoin="round" strokeLinecap="round" />
                                    </svg>
                                    <span>Add to cart</span>
                                </button>
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