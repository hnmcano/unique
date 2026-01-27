function FormularioPedido({ data, handleChangeClient, handledChangeEntrega, handleBlurCEP }) {

    return (
        <>
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
        </>
    )

}

export default FormularioPedido;