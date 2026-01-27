import { Link } from "react-router-dom";

import { useCheckout } from "../../contexts/CheckoutContext";

import api from "../../api/api";

import "../../styles/Checkout.css";

function FormularioPedido({}) {
        const { data, setData} = useCheckout();

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

    const handleBlurCEP = async (event) => {
        const cep = event.target.value.replace(/[^0-9]/g, '');
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
        <>
            <div className="Formulario-Pedidos">
                <form>
                    {/* Campos de Dados Pessoais */}
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="name">Nome Completo:</label>
                        <input className="Entrada-Formulario" type="text" id="nome" name="nome" value={data.cliente.nome} onChange={handleChangeClient} required />
                    </div>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="email">E-mail:</label>
                        <input className="Entrada-Formulario" type="email" id="email" name="email" value={data.cliente.email} onChange={handleChangeClient} required />
                    </div>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="telefone">Telefone:</label>
                        <input className="Entrada-Formulario"// <-- Handler específico para a máscara
                            type="tel" id="telefone" name="telefone" value={data.cliente.telefone} onChange={handleChangeClient} required inputMode="numeric" 
                            maxLength="15" // (XX) XXXXX-XXXX
                        />
                    </div>
                    {/* Campo CEP */}
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cep">CEP:</label>
                        <div className="Grupo-Formulario-concat">
                            <input 
                                className="Entrada-Formulario"
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
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="rua">Rua/Endereço:</label>
                            {/* O valor vem do estado e está desabilitado */}
                            <input className="Entrada-Formulario" type="text" id="rua" name="endereco" value={data.entrega.endereco} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                        </div>
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="numero">Número:</label>
                            {/* O número é digitado pelo usuário */}
                            <input className="Entrada-Formulario" type="text" id="numero" name="numero" value={data.entrega.numero} onChange={handledChangeEntrega} required />
                        </div>
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="complemento">Complemento:</label>
                        <input className="Entrada-Formulario" type="text" id="complemento" name="complemento" value={data.entrega.complemento} onChange={handledChangeEntrega}/>
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="bairro">Bairro:</label>
                        <input className="Entrada-Formulario"type="text" id="bairro" name="bairro" value={data.entrega.bairro} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cidade">Cidade:</label>
                        <input className="Entrada-Formulario" type="text" id="cidade" name="cidade" value={data.entrega.cidade} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="estado">Estado:</label>
                        <input className="Entrada-Formulario" type="text" id="estado" name="estado" value={data.entrega.estado} onChange={handledChangeEntrega} disabled style={{ color: "white" }} />
                    </div>

                    {/* Botões */}
                    <div className="Botoes-Checkout">
                        <button className="voltar" type="button">Cancelar</button>
                        <Link to="/Checkout/Etapa2">
                            <button className="continuar-Checkout">Continuar</button>
                        </Link>
                    </div>
                </form>
            </div>
        </>
    )

}

export default FormularioPedido;