function DadosLojaCatalago({estabelecimento, status}) {

    return (
        <>
            <div className="logotipo-hookah">
                <img className="logotipo" src={`data:image/png;base64,${estabelecimento?.logo_base64}`} alt="Logo"/>
            </div>
            <div className="data">
                <div className="status-container">
                    <label className={status === "ABERTO" ? "status_aberto" : "status_fechado"}>{status}</label>
                </div>
                <div className="infos">
                    <div className="infos-data">
                        <div className="montserrat-data">Endereço: {estabelecimento?.endereco}</div>
                    </div>
                    <div className="infos-data">
                        <div className="montserrat-data">Telefone: {estabelecimento?.telefone} | Instagram: {estabelecimento?.instagram}</div>
                    </div>
                    <div className="infos-data">
                        <div className="montserrat-data"> Horário: 13:00 às 17:00</div>
                    </div>
                </div>
            </div>
        </>
    )

}

export default DadosLojaCatalago;