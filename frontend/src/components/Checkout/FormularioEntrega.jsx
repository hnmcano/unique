import { Link, useNavigate } from "react-router-dom";
import api from "../../api/api";
import axios from "axios";
import { useEffect, useRef, useState } from "react";
import { useCheckout } from "../../contexts/CheckoutContext";
import { MapContainer, TileLayer, Marker } from "react-leaflet";
import { ButtonBack, ButtonNext } from "./buttons/ButtonsCheckout";

function FormularioEntrega() {
    const Navigate = useNavigate();
    const {data, setData} = useCheckout();
    const [checked, setchecked] = useState(true);
    const [position, setPosition] = useState(null);
    const refs = useRef([]);

    console.log(data);

    const focusNextInput = (index) => {
        refs.current[index + 1]?.focus();
    };

    const buscarCoordenadas = async (endereco) => {

        console.log(endereco);

        const res = await fetch(
            `https://nominatim.openstreetmap.org/search?format=json&q=${endereco}`
        );

        const data = await res.json();

        if (data.length > 0) {
                setPosition([
                parseFloat(data[0].lat),
                parseFloat(data[0].lon),
            ]);
        }

        console.log(position);

    };

    useEffect(() => {

        if (!data.entrega.endereco || !data.entrega.numero) return;

        buscarCoordenadas(
            `${data.entrega.endereco}, ${data.entrega.numero}, ${data.entrega.bairro}, ${data.entrega.cidade}, ${data.entrega.estado}`
        );

    }, [data.entrega.numero, data.entrega.endereco]);


    const handleBlurCEP = async (event) => {
        if (event.target.value !== "") {
            const numero = event.target.value;
            const cep = event.target.value.replace(/[^0-9]/g, '');
            if (cep.length === 8) {
                try {
                    const res = await axios.get(`https://viacep.com.br/ws/${cep}/json/`);
                    const endereco = await res.data;
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

        
                } catch (error) {
                    console.log(error);
                }
            }
        
        }
    }

    const handledChangeEntrega = (event) =>{
        const { name, value } = event.target;

        let newValue = value === "-" ? "": value;

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
        if (data.entrega.cep && data.entrega.endereco && data.entrega.numero && data.entrega.bairro && data.entrega.cidade && data.entrega.estado){        
            Navigate("/Checkout/Etapa3"); 
        }else {
            alert("Por favor, preencha todos os campos obrigatórios.");
        }
        
    }

    return (
        <>
            {/* Campo CEP */}
            <div className="Formulario-Entrega"> 
                <form>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cep">CEP:<label style={{"color": "red"}}>* </label></label>
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
                                onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(0);}}} 
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
                            style={{  color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }} />
                        </div>
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="numero">Número:<label style={{"color": "red"}}>* </label></label>
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
                            onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(1);}}}                             
                            required />
                        </div>
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="complemento">Complemento:<label style={{"color": "red"}}>* </label></label>
                        <input className="Entrada-Formulario" 
                        type="text" id="complemento" 
                        name="complemento" 
                        value={data.entrega.complemento} 
                        onChange={handledChangeEntrega}                             
                        ref={(el) => (refs.current[2] = el)}
                        enterKeyHint="next"
                        onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(2);}}}  
                        />
                    </div>

                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="bairro">Bairro:</label>
                        <input className="Entrada-Formulario"type="text" id="bairro" name="bairro" value={data.entrega.bairro} onChange={handledChangeEntrega} disabled style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868" }} />
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="cidade">Cidade:</label>
                        <input className="Entrada-Formulario" type="text" id="cidade" name="cidade" value={data.entrega.cidade} onChange={handledChangeEntrega} disabled style={{ color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868"  }} />
                    </div>
                    
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="estado">Estado:</label>
                        <input className="Entrada-Formulario" type="text" id="estado" name="estado" value={data.entrega.estado} onChange={handledChangeEntrega} disabled style={{color: "white", cursor: "not-allowed", pointerEvents: "none", backgroundColor: "#686868"  }} />
                    </div>
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
                        <ButtonBack/>
                    </Link>
                    <ButtonNext checked={checked} handledSubmit={handledSubmit}/>
                </div>
            </div>
        </>
    );
}

export default FormularioEntrega;