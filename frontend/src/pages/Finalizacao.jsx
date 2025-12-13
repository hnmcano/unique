import "../styles/Pedidos.css";
import "../styles/Carrinho.css"// Descomente se for usar
import { useCarrinho } from "../hooks/useCarrinho";
import ModalShopping from "../components/Carrinho";
import { Link, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/api";

function DataFinalizacao() {
    const { produtos, fetchCarrinho } = useCarrinho();
    const [modalShoppingOpen, setModalShoppingOpen] = useState(false);
    const [ data, setData] = useState({

        "itens": [
            {
                produto_id: 0,
                quantidade: 0,
                valor_unitario: 0,
            }
        ],

        metodo_pagamento: "",
        valor_total: 0,
        observacoes: "",

        "cliente": {
            nome: "",
            email: "",
            telefone: "",
        },

        "entrega": {
        cep: "",
        endereco: "",
        numero: "",
        bairro: "",
        cidade: "",
        estado: "",
        complemento: "",
        referencia: "",
        taxa_entrega: 7.0,
    }
    });


    const totalValor = produtos.reduce((acc, p) => acc + p.valor_total, 0);
    const totalQuantidade = produtos.reduce((acc, p) => acc + p.quantidade, 0);

    const listaPayment = [ 
        {"id": "cc","tipo": "Cartão de Credito"},
        {"id": "cd", "tipo": "Cartão de Debito"}, 
        {"id": "pix", "tipo": "Pix"}, 
        {"id": "din", "tipo": "Dinheiro"}
    ]


    const openModal = () => setModalShoppingOpen(true)
    const closeModal = () => setModalShoppingOpen(false)

    useEffect(() => {
        if (closeModal){
            fetchCarrinho();
        }
    }, [modalShoppingOpen, fetchCarrinho]);

    const handleChangeClient = (event) => {
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            cliente: {
                ...prevState.cliente,
                [name]: value
            }

        }));
    };

    const handledChangeEntrega = (event) =>{
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            entrega: {
                ...prevState.entrega,
                [name]: value
            }
        }));
    }    

    const handledChangeInfos = (event) => {
        const { name, value } = event.target;
        setData(prevState => ({
            ...prevState,
            [name]: value,
        }));

    }

    useEffect(() => {
        setData(prevState => ({
            ...prevState,
            itens: produtos.map(p => ({
                produto_id: p.produto_id,
                quantidade: p.quantidade,
                valor_unitario: p.preco_venda

            })),
            valor_total: totalValor + 7.0,
            
        }));
    }, [produtos, totalValor, totalQuantidade]);

    const handledSubmit = async (event) => {
        event.preventDefault();
        console.log(data);
        const response = await api.post("/pedidos/react", data);
        console.log(response.data);

    }

    const handleBlurCEP = async (event) => {
        const cep = event.target.value.replace(/[^0-9]/g, '');
        console.log(cep);
        if (cep.length === 8) {
            try {
                const res = await api.get(`https://viacep.com.br/ws/${cep}/json/`);
                const endereco = await res.data;
                setData(prevState => ({
                    ...prevState,
                    entrega: {
                        ...prevState.entrega,
                        cep: endereco.cep,
                        endereco: endereco.logradouro,
                        bairro: endereco.bairro,
                        cidade: endereco.localidade,
                        estado: endereco.uf,
                    }
                }));

            } catch (error) {
                console.log(error);
            }
        }
    }

    return (
        <div className="container__">
            <div className="data-finalizacao">
                <div className="finalizacao-data">
                    <form>
                        {/* Campos de Dados Pessoais */}
                        <div className="form-group">
                            <label htmlFor="name">Nome Completo:</label>
                            <input  type="text" id="nome" name="nome" value={data.cliente.nome} onChange={handleChangeClient} required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="email">E-mail:</label>
                            <input className="email" type="email" id="email" name="email" value={data.cliente.email} onChange={handleChangeClient} required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="telefone">Telefone:</label>
                            <input // <-- Handler específico para a máscara
                                type="tel" id="telefone" name="telefone" value={data.cliente.telefone} onChange={handleChangeClient} required inputMode="numeric" 
                                maxLength="15" // (XX) XXXXX-XXXX
                            />
                        </div>
                        
                        {/* Campo CEP */}
                        <div className="form-group">
                            <label htmlFor="cep">CEP:</label>
                            <div className="form-group-concat">
                                <input 
                                    className="cep" 
                                    type="text" 
                                    id="cep" 
                                    name="cep"
                                    value={data.entrega.cep}
                                    onChange={handledChangeEntrega}
                                    onBlur={handleBlurCEP}
                                    required
                                    maxLength="9" // 00000-000
                                    
                                />
                                {/* Removido o botão 'Buscar' manual, agora é automático via useEffect */}
                            </div>
                        </div>
                        
                        {/* Campos de Endereço */}
                        <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
                            <div className="form-group">
                                <label htmlFor="rua">Rua/Endereço:</label>
                                {/* O valor vem do estado e está desabilitado */}
                                <input type="text" id="rua" name="endereco" value={data.entrega.endereco} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="numero">Número:</label>
                                {/* O número é digitado pelo usuário */}
                                <input type="text" id="numero" name="numero" value={data.entrega.numero} onChange={handledChangeEntrega} required />
                            </div>
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="complemento">Complemento:</label>
                            <input type="text" id="complemento" name="complemento" value={data.entrega.complemento} onChange={handledChangeEntrega}/>
                        </div>

                        <div className="form-group">
                            <label htmlFor="bairro">Bairro:</label>
                            <input type="text" id="bairro" name="bairro" value={data.entrega.bairro} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="cidade">Cidade:</label>
                            <input  type="text" id="cidade" name="cidade" value={data.entrega.cidade} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="estado">Estado:</label>
                            <input  type="text" id="estado" name="estado" value={data.entrega.estado} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                        </div>

                        {/* Botões */}
                    </form>
                </div>
            </div>
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
                            <td style={{"text-align": "left"}} colSpan="2">Total</td>
                            <td style={{"margin": "5px",}}>{totalQuantidade}</td>
                            <td style={{"margin": "5px",}} className="value-produto"><label>R$</label>{totalValor.toFixed(2)}</td>
                        </tr>
                    </tbody>
                </table>
                <div className="dropdowns">
                    <div className="div-dropdown-payment">
                        <label>Metodo de Pagamento</label>
                        <select name="metodo_pagamento" value={data.metodo_pagamento} onChange={handledChangeInfos} style={{"width": "220px", "margin-top": "10px", "height": "25px", "border-radius": "5px"}}>
                            {listaPayment.map(formas => (
                                <option   key={formas.id} value={formas.id}>{formas.tipo}</option>
                            ))}
                        </select>
                    </div>
                    <div className="div-dropdown-payment" disabled>
                        <label>Bandeira</label>
                        <select disabled style={{"width": "220px", "margin-top": "10px", "height": "25px", "border-radius": "5px"}}>
                            {listaPayment.map(formas => (
                                <option value={formas.id}>{formas.tipo}</option>
                            ))}
                        </select>
                    </div>
                </div>
                <div className="observacoes">
                    <label style={{"width": "75%"}}>OBSERVAÇÕES</label>
                    <input className="input-observacoes" id="inputObs" type="text" name="observacoes" value={data.observacoes} onChange={handledChangeInfos}></input>
                </div>
                <div className="botoes-finalizacao">
                    <button onClick={handledSubmit} className="botao-finalizar-compra" type="submit">Finalizar Compra</button>
                    <Link to="/">
                        <button className="botao-cancelar-compra" type="button">Continuar Comprando</button>
                    </Link>

                    <button onClick={openModal} className="botao-cancelar-compra" type="button"><ModalShopping openModal={modalShoppingOpen} closeModal={closeModal}></ModalShopping>Editar Carrinho</button>
                    <button className="botao-cancelar-compra" type="button">Limpar Dados</button>
                </div>
            </div>
        </div>
    );
}

export default DataFinalizacao;