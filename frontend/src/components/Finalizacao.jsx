import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import "../styles/Finalizacao.css";
import { usePedidos } from "../hooks/pedidos"; // Descomente se for usar


function DataFinalizacao() {

    return (
        <div className="container__">
            <div className="data-finalizacao">
                <h1>Finalizar Compra</h1>
                <div className="finalizacao-data">
                    <form onSubmit={handledData} disabled={fecthLoading}>
                        {/* Campos de Dados Pessoais */}
                        <div className="form-group">
                            <label htmlFor="name">Nome Completo:</label>
                            <input value={formData.name} onChange={handleChange} type="text" id="name" name="name" required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="email">E-mail:</label>
                            <input value={formData.email} onChange={handleChange} className="email" type="email" id="email" name="email" required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="telefone">Telefone:</label>
                            <input 
                                value={formData.telefone} 
                                onChange={handleTelefoneChange} // <-- Handler específico para a máscara
                                type="tel" id="telefone" name="telefone" required inputMode="numeric" 
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
                                    required 
                                    value={formData.cep} 
                                    onChange={handleCepChange} // <-- Handler específico para o CEP
                                    maxLength="9" // 00000-000
                                />
                                {/* Removido o botão 'Buscar' manual, agora é automático via useEffect */}
                                {loading && <p>Buscando...</p>}
                            </div>
                        </div>
                        
                        {/* Campos de Endereço */}
                        <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
                            <div className="form-group">
                                <label htmlFor="rua">Rua/Endereço:</label>
                                {/* O valor vem do estado e está desabilitado */}
                                <input value={formData.rua} type="text" id="rua" name="rua" disabled style={{ color: "white" }} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="numero">Número:</label>
                                {/* O número é digitado pelo usuário */}
                                <input value={formData.numero} onChange={handleChange} type="text" id="numero" name="numero" required />
                            </div>
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="complemento">Complemento:</label>
                            <input value={formData.complemento} onChange={handleChange} type="text" id="complemento" name="complemento" />
                        </div>

                        <div className="form-group">
                            <label htmlFor="bairro">Bairro:</label>
                            <input value={formData.bairro} type="text" id="bairro" name="bairro" disabled style={{ color: "white" }} />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="cidade">Cidade:</label>
                            <input value={formData.cidade} type="text" id="cidade" name="cidade" disabled style={{ color: "white" }} />
                        </div>
                        
                        <div className="form-group">
                            <label htmlFor="estado">Estado:</label>
                            <input value={formData.estado} type="text" id="estado" name="estado" disabled style={{ color: "white" }} />
                        </div>

                        {/* Botões */}
                        <div>
                            <button className="finalizar" type="submit">Finalizar Compra</button>
                            <button type="button" onClick={handleReset}>Limpar Dados</button>
                        </div>
                    </form>
                </div>
            </div>
            <div className="data-carrinho"> 
            </div>
        </div>
    );
}

export default DataFinalizacao;