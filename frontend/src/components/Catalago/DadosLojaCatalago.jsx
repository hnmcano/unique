import { useEstabelecimento } from "../../contexts/EstabelecimentoContext";
import { useHorarios } from "../../contexts/HorariosContext";
import Horarios from "../../pages/Horarios";


function DadosLojaCatalago({}) {
    const { estabelecimento, loading } = useEstabelecimento();
    const status = estabelecimento?.online === true ? "ABERTO" : "FECHADO";
    const style = estabelecimento?.cor_layout !== null
        ? { color: estabelecimento?.cor_layout, marginTop: 0 }
        : {};

    const classText = estabelecimento?.cor_layout === null ? "subtitle" : "";
    const {opencard, setOpenCard} = useHorarios();

    return (
        <>
            <div className="logotipo-hookah">
                <img className="logotipo" src={`data:image/png;base64,${estabelecimento?.logo_img}`} alt="Logo"/>
            </div>
            <div className="data">
                <div className="status-container">
                    <label className={status === "ABERTO" ? "status_aberto" : "status_fechado"}>{status}</label>
                </div>
                <header className="infos">
                    <h1>{estabelecimento?.nome_fantasia}</h1>
                    <p style={style} className={classText}>{estabelecimento?.descricao}</p>
                </header>
                <div className="infos">
                    <div className="infos">
                        <a>Endereço</a>
                        <a style={style} className={classText}>{estabelecimento?.endereco}</a>
                    </div>
                    
                    <div className="infos">
                        <div onClick={() => setOpenCard(true)} className="horarios" style={{backgroundColor: estabelecimento?.cor_layout}}>
                            <span>HORARIOS</span>
                            <Horarios></Horarios>
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