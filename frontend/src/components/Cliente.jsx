import React, { useState, useEffect } from "react";
import "../styles/Cliente.css"

function DataClient() {
    return (
        <div className="client-delivery">
            <div className="client-data">
                <div className="user-data-title">
                    <h2>Dados do Cliente</h2>
                </div>
                <div className="data-name-input">
                    <label style={{"color": "white", "marginRight": "10px", "fontFamily": "Arial"}}>NOME:</label>
                    <input className="name-input" type="text" />
                </div>
                <div className="data-dat-input">
                    <label>Nome:</label>
                    <input type="text" />
                </div>
            </div>
            <div className="adress-data"></div>
        </div>
    )
}


export default DataClient;
