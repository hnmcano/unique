function FormasPagPedido({data, handledChangeInfos}) {

    const listaPayment = [ 
        {"id": "cc","tipo": "Cartão de Credito"},
        {"id": "cd", "tipo": "Cartão de Debito"}, 
        {"id": "pix", "tipo": "Pix"}, 
        {"id": "din", "tipo": "Dinheiro"}
    ]

    return (
        <>
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
        </>
    )

}


export default FormasPagPedido;