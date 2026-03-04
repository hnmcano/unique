import { useEstabelecimento } from "../../contexts/EstabelecimentoContext";


function DadosLojaCatalago({}) {
    const { estabelecimento, loading } = useEstabelecimento();
    const status = estabelecimento?.online === true ? "ABERTO" : "FECHADO";
    
    return (
        <>
            <div className="logotipo-hookah">
                <img className="logotipo" src={`data:image/png;base64,${estabelecimento?.logo_img}`} alt="Logo"/>
            </div>
            <div>
                <div class="status-badge">ABERTO</div>
                <header>
                    <h1>Hookah Shisha</h1>
                    <p class="subtitle">Tabacaria & Lounge</p>
                </header>
                <div class="info-container">
                    <div class="info-item">
                    <span class="label">Endereço</span>
                    <span class="value accent">ONLINE</span>
                    </div>
                    
                    <div class="info-item">
                    <span class="label">Horário</span>
                    <span class="value">13:00 às 17:00</span>
                    </div>
                </div>
                <footer class="contact-bar">
                    <a href="https://wa.me/5514996323908" class="contact-link">📞 (14) 99632-3908</a>
                    <a href="#" class="contact-link">📸 @HookahshishaTabacaria</a>
                </footer>
            </div>
        </>
    )

}

export default DadosLojaCatalago;