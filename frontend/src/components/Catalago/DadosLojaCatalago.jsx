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
                        <a>Endereço</a>
                        <a className="endereco-definido">{estabelecimento?.endereco}</a>
                    </div>
                    <div className="infos">
                        <span class="label">Horário</span>
                        <span class="value">13:00 às 17:00</span>
                    </div>
                </div>
                <footer className="infos-contact">
                    <span href="https://wa.me/5514996323908" class="contact-link">📞 {estabelecimento?.telefone}</span>
                    <span href="#" class="contact-link">📸 {estabelecimento?.rede_social}</span>
                </footer>
            </div>
        </>
    )

}

export default DadosLojaCatalago;