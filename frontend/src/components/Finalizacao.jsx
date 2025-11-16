import React, { useState, useEffect } from "react";
import "../styles/Finalizacao.css"

function DataFinalizacao() {
    return (
        <div className="container__">
            <div className="data-finalizacao">
                <h1>Finalizar Compra</h1>
                <div className="finalizacao-info">
                    <div className="information">
                        <label style={{"margin": "45px" }}>
                            Dados para identificação da entrega, campos obrigatórios seram marcados com (*). 
                        </label>
                    </div>
                </div>
                <div className="finalizacao-data">
                    <form>

                    </form>
                </div>
            </div>
            <div className="data-carrinho">
                
            </div>
        </div>
    )
}


export default DataFinalizacao;
