import { Link, useNavigate } from "react-router-dom";
import api from "../../api/api";
import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useCheckout } from "../../contexts/CheckoutContext";
import { MapContainer, TileLayer, Marker } from "react-leaflet";
import { ButtonBack, ButtonNext } from "./buttons/ButtonsCheckout";
import { calcularTaxaEntrega } from "../../utils/distanceUtils"; // ⭐ Importar função

function FormularioEntrega() {
    const Navigate = useNavigate();
    const { data, setData } = useCheckout();
    const [checked, setchecked] = useState(true);
    const [position, setPosition] = useState(null);
    const [taxaEntrega, setTaxaEntrega] = useState(null); // ⭐ Novo estado
    const [distanciaKm, setDistanciaKm] = useState(null); // ⭐ Novo estado
    const [carregando, setCarregando] = useState(true); // ⭐ Novo estado
    const [erro, setErro] = useState(null); // ⭐ Novo estado
    
    const [tabelaFrete, setTabelaFrete] = useState([]);
    const [coordsEstabelecimento, setCoordsEstabelecimento] = useState(null);
    
    const refs = useRef([]);

    useEffect(() => {
        const carregarDados = async () => {
            try {
                setCarregando(true);
                setErro(null);

                // Busca tabela de frete
                const resFrete = await api.get('/estabelecimento/taxas-km');
                setTabelaFrete(resFrete.data);
                console.log(resFrete.data);

                // Busca coordenadas do estabelecimento
                const resEstab = await api.get('/estabelecimento/react/coordenadas-estabelecimento');
                setCoordsEstabelecimento({
                    lat: resEstab.data.lat,
                    lon: resEstab.data.lon
                });

                console.log(resEstab.data);

                console.log("✅ Dados de entrega carregados com sucesso");
            } catch (error) {
                console.error("❌ Erro ao carregar dados de entrega:", error);
                setErro("Erro ao carregar informações de entrega");
            } finally {
                setCarregando(false);
            }
        };

        carregarDados();
    }, []);

    const focusNextInput = (index) => {
        refs.current[index + 1]?.focus();
    };

    const buscarCoordenadas = async (endereco) => {
        console.log("🔍 Buscando coordenadas para:", endereco);

        try {
            const res = await fetch(
                `https://nominatim.openstreetmap.org/search?format=json&q=${endereco}`
            );
        
            console.log(res);

            const dataRes = await res.json();

            if (dataRes.length > 0) {
                const novasCoords = {
                    lat: parseFloat(dataRes[0].lat),
                    lon: parseFloat(dataRes[0].lon)
                };
                
                setPosition([novasCoords.lat, novasCoords.lon]);

                // ⭐ CALCULA A TAXA APENAS SE TIVER OS DADOS DO BACKEND
                if (coordsEstabelecimento && tabelaFrete.length > 0) {
                    const resultado = calcularTaxaEntrega(
                        novasCoords,
                        coordsEstabelecimento,
                        tabelaFrete
                    );
                    
                    if (resultado) {
                        setDistanciaKm(resultado.distancia);
                        setTaxaEntrega(resultado);

                        // ⭐ Salva a taxa no contexto do checkout
                        setData(prevState => ({
                            ...prevState,
                            entrega: {
                                ...prevState.entrega,
                                taxa_entrega: resultado.valor,
                                distancia: resultado.distancia,
                                faixa_km: `${resultado.km_minimo}-${resultado.km_maximo}`
                            }
                        }));
                        setErro(null);
                    } else {
                        console.warn("⚠️ Endereço fora da área de cobertura");
                        setDistanciaKm(null);
                        setTaxaEntrega(null);
                        setErro("Endereço fora da área de cobertura");
                    }
                }
            }
        } catch (error) {
            console.error("❌ Erro ao buscar coordenadas:", error);
            setErro("Erro ao buscar localização");
        }
    };

    useEffect(() => {
        if (!data.entrega.endereco || !data.entrega.numero) return;
        if (!coordsEstabelecimento || tabelaFrete.length === 0) return;
        buscarCoordenadas(
            `${data.entrega.endereco}, ${data.entrega.numero}`
        );
    }, [data.entrega.numero, data.entrega.endereco, coordsEstabelecimento, tabelaFrete]);

    const handleBlurCEP = async (event) => {
        if (event.target.value !== "") {
            const numero = event.target.value;
            const cep = event.target.value.replace(/[^0-9]/g, '');
            if (cep.length === 8) {
                try {
                    const res = await axios.get(`https://viacep.com.br/ws/${cep}/json/`);
                    const endereco = await res.data;
                    
                    if (endereco.erro) {
                        setErro("CEP inválido");
                        return;
                    }

                    const cepAtualizado = endereco.cep.replace(/[^0-8]/g, '');
                    setData(prevState => ({
                        ...prevState,
                        entrega: {
                            ...prevState.entrega,
                            cep: cepAtualizado,
                            endereco: endereco.logradouro,
                            bairro: endereco.bairro,
                            cidade: endereco.localidade,
                            estado: endereco.uf,
                        }
                    }));
                    setErro(null);
                } catch (error) {
                    console.log(error);
                    setErro("Erro ao validar CEP");
                }
            }
        }
    }

    const handledChangeEntrega = (event) => {
        const { name, value } = event.target;

        let newValue = value === "-" ? "" : value;

        setData(prevState => ({
            ...prevState,
            entrega: {
                ...prevState.entrega,
                [name]: newValue
            }
        }));
    }

    const handledSubmit = (event) => {
        event.preventDefault();
        
        // ⭐ VERIFICA SE TEM TAXA CALCULADA
        if (!taxaEntrega) {
            alert("Por favor, complete o endereço. Distância não pode ser calculada.");
            return;
        }

        if (data.entrega.cep && data.entrega.endereco && data.entrega.numero && 
            data.entrega.bairro && data.entrega.cidade && data.entrega.estado) {
            Navigate("/Checkout/Etapa3");
        } else {
            alert("Por favor, preencha todos os campos obrigatórios.");
        }
    }

    // ⭐ Mostra loading enquanto busca dados
    if (carregando) {
        return (
            <div className="Formulario-Entrega">
                <p style={{ textAlign: "center", padding: "20px" }}>
                    ⏳ Carregando informações de entrega...
                </p>
            </div>
        );
    }

    return (
        <>
            {/* Campo CEP */}
            <div className="Formulario-Entrega">
                {/* ⭐ MOSTRA ERRO SE HOUVER */}
                {erro && (
                    <div style={{
                        padding: "10px",
                        marginBottom: "15px",
                        backgroundColor: "#ffebee",
                        borderLeft: "4px solid #f44336",
                        borderRadius: "4px",
                        color: "#c62828"
                    }}>
                        ⚠️ {erro}
                    </div>
                )}

                <form>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cep">CEP:<label style={{ "color": "red" }}>* </label></label>
                        <div className="Grupo-Formulario-concat">
                            <input
                                className="Entrada-Formulario"
                                type="text"
                                id="cep"
                                name="cep"
                                value={data.entrega.cep}
                                onChange={handledChangeEntrega}
                                onBlur={handleBlurCEP}
                                required
                                maxLength="9" // 00000-000
                                ref={(el) => (refs.current[0] = el)}
                                enterKeyHint="next"
                                onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); focusNextInput(0); } }}
                                placeholder="00000-000"
                            />
                            {/* Removido o botão 'Buscar' manual, agora é automático via useEffect */}
                        </div>
                    </div>
                    {/* Campos de Endereço */}
                    <div style={{ display: "flex", flexDirection: "row", gap: "10px" }}>
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="rua">Rua/Endereço:</label>
                            {/* O valor vem do estado e está desabilitado */}
                            <input
                                className="Entrada-Formulario"
                                type="text"
                                id="rua"
                                name="endereco"
                                value={data.entrega.endereco}
                                onChange={handledChangeEntrega}
                                disabled
                                style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }}
                            />
                        </div>
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="numero">Número:<label style={{ "color": "red" }}>* </label></label>
                            {/* O número é digitado pelo usuário */}
                            <input
                                className="Entrada-Formulario"
                                type="text"
                                id="numero"
                                name="numero"
                                value={data.entrega.numero}
                                onChange={handledChangeEntrega}
                                ref={(el) => (refs.current[1] = el)}
                                enterKeyHint="next"
                                onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); focusNextInput(1); } }}
                                required
                                placeholder="Ex: 123"
                            />
                        </div>
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="complemento">Complemento:<label style={{ "color": "red" }}>* </label></label>
                        <input
                            className="Entrada-Formulario"
                            type="text"
                            id="complemento"
                            name="complemento"
                            value={data.entrega.complemento}
                            onChange={handledChangeEntrega}
                            ref={(el) => (refs.current[2] = el)}
                            enterKeyHint="next"
                            onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); focusNextInput(2); } }}
                            placeholder="Apto, sala, etc"
                        />
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="bairro">Bairro:</label>
                        <input
                            className="Entrada-Formulario"
                            type="text"
                            id="bairro"
                            name="bairro"
                            value={data.entrega.bairro}
                            onChange={handledChangeEntrega}
                            disabled
                            style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }}
                        />
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cidade">Cidade:</label>
                        <input
                            className="Entrada-Formulario"
                            type="text"
                            id="cidade"
                            name="cidade"
                            value={data.entrega.cidade}
                            onChange={handledChangeEntrega}
                            disabled
                            style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }}
                        />
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="estado">Estado:</label>
                        <input
                            className="Entrada-Formulario"
                            type="text"
                            id="estado"
                            name="estado"
                            value={data.entrega.estado}
                            onChange={handledChangeEntrega}
                            disabled
                            style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }}
                        />
                    </div>

                    {/* ⭐ CARD COM DISTÂNCIA E TAXA DE ENTREGA */}
                    {distanciaKm && taxaEntrega && (
                        <div style={{
                            marginTop: "20px",
                            padding: "15px",
                            backgroundColor: "#e8f5e9",
                            borderRadius: "8px",
                            border: "2px solid #4CAF50",
                            boxShadow: "0 2px 4px rgba(76, 175, 80, 0.2)",
                            width: "100%",
                            maxWidth: "400px"
                        }}>
                            <hr style={{ margin: "10px 0", borderColor: "#4CAF50", opacity: 0.3 }} />

                            <p style={{ margin: "8px 0", fontSize: "16px", fontWeight: "bold", color: "#1b5e20" }}>
                                💰 Taxa de Entrega
                            </p>
                            <p style={{ margin: "5px 0", fontSize: "24px", fontWeight: "bold", color: "#4CAF50" }}>
                                R$ {taxaEntrega.valor.toFixed(2)}
                            </p>
                        </div>
                    )}
                </form>

                {position && (
                    <div className="map-container">
                        <MapContainer
                            center={position}
                            zoom={16}
                            className="map"
                        >
                            <TileLayer
                                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            />
                            <Marker position={position} />
                        </MapContainer>
                    </div>
                )}

                {/* Botões */}
                <div className="Botoes-Checkout">
                    <Link to="/Checkout/Etapa1">
                        <ButtonBack />
                    </Link>
                    <ButtonNext checked={checked} handledSubmit={handledSubmit} />
                </div>
            </div>
        </>
    );
}

export default FormularioEntrega;
