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
                    <div className="itens-product-img">
                        <img className="img-product" src={imagemUrl(produtos.imagem)} alt="imagem produto"/>
                    </div>
                    <div className="data-itens-unique">
                        <div className="data-itens-unique-name">
                            {produtos.nome}
                        </div>
                        <div className="data-itens-unique-description">
                            {produtos.descricao}
                        </div>
                        <div className="data-itens-unique-select">
                            <div className="data-itens-unique-select-quantity">
                                <button onClick={() => addProduct(categoria, produtos)} className="data-itens-unique-select-adicionar">ADICIONAR</button>
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