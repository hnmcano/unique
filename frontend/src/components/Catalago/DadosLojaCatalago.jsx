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
                    <h1>{estabelecimento?.nome_fantasia}</h1>
                    <p className="subtitle">Tabacaria</p>
                </header>
                <div className="infos">
                    <div className="infos">
                        <a>Endereço</a>
                        <a className="endereco-definido">{estabelecimento?.endereco}</a>
                    </div>
                    <div className="infos">
                        <span class="label">Horário</span>
                        <span class="value"> Seg à Sex: 14:00 às 22:00</span>
                        <div style={{ display: "flex", flexDirection: "row", gap: 10,}}>
                            <span class="value"> Sab: 15:00 às 21:00</span>
                            <span class="value"> Dom: 14:00 às 18:00</span>
                        </div>
                    </div>
                </div>
                <footer className="infos-contact">
                    <span onClick={() => window.open("https://wa.me/" + estabelecimento?.telefone)} className="contact-link">📞 {estabelecimento?.telefone}</span>
                    <span onClick={() => window.open("https://www.instagram.com/" + estabelecimento?.rede_social)} className="contact-link">📸 {estabelecimento?.rede_social}</span>
                </footer>
            </div>
        </>
    )

}

export default DadosLojaCatalago;