import { useEstabelecimento } from "../../contexts/EstabelecimentoContext";


function DadosLojaCatalago({}) {
    const { estabelecimento, loading } = useEstabelecimento();
    const status = estabelecimento?.online === true ? "ABERTO" : "FECHADO";
    
    return (
        <>
            <div className="logotipo-hookah">
                <img className="logotipo" src={`data:image/png;base64,${estabelecimento?.logo_img}`} alt="Logo"/>
            </div>
            <div className="data">
                <div class="status-container">
                    <label className={status === "ABERTO" ? "status_aberto" : "status_fechado"}>{status}</label>
                </div>
                <header className="infos">
                    <h1>Hookah Shisha</h1>
                    <p className="subtitle">Tabacaria</p>
                </header>
                <div className="infos">
                    <div className="infos">
                        <span className="montserrat-data">Endereço: {estabelecimento?.endereco}</span>
                    </div>
                    <div className="infos">
                        <span class="label">Horário</span>
                        <span class="value">13:00 às 17:00</span>
                    </div>
                </div>
                <footer className="infos">
                    <a href="https://wa.me/5514996323908" class="contact-link">📞 {estabelecimento?.telefone}</a>
                    <a href="#" class="contact-link">📸 {estabelecimento?.rede_social}</a>
                </footer>
            </div>
        </>
    )

}

export default DadosLojaCatalago;