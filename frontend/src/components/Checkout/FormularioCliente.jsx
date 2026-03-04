import { Link, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { useRef } from "react";

import { useCheckout } from "../../contexts/CheckoutContext";
import { ButtonNext, ButtonBack } from "./buttons/ButtonsCheckout";

import "../../styles/Checkout.css";

function FormularioCliente() {
    const onlyNumbers = (v) => v.replace(/\D/g, "");
    const [checked, setChecked] = useState(false);
    const { data, setData} = useCheckout();
    const navigate = useNavigate();
    const refs = useRef([]);
    const [formTelefone, setFormTelefone] = useState({
        telefone: "",
    });

    const MaskTelefone = (value) => {
        value = onlyNumbers(value);

        if (value.length <= 10) {
            value = value.replace(/^(\d{2})(\d)/, "($1) $2");
            value = value.replace(/(\d{4})(\d)/, "$1-$2");
        } else {
            value = value.replace(/^(\d{2})(\d)/, "($1) $2");
            value = value.replace(/(\d{5})(\d)/, "$1-$2");
        }

        return value;
    }

    const focusNextInput = (index) => {
        refs.current[index + 1]?.focus();
    };

    const handleTelefoneChange = (e) => {
        const masked = MaskTelefone(e.target.value);

        setFormTelefone((prev) => ({
            ...prev,
            telefone: masked,
        }));
    };

    const handleChangeClient = (event) => {
        const { name, value } = event.target;

        if (name === "observacoes") {
            setData((prev) => ({
                ...prev,
                observacoes: value,
            }));
        } else {
            setData(prevState => ({
                ...prevState,
                cliente: {
                    ...prevState.cliente,
                    [name]: value
                }
            }));
        }
    };

    useEffect(() => {
        if (data.cliente.telefone) {
            setFormTelefone({
                telefone: MaskTelefone(data.cliente.telefone),
            });
        }
    }, [data.cliente.telefone]);

    const handledSubmit = (e) => {
        e.preventDefault();

        const clienteFinal = {
            ...data.cliente,
            telefone: onlyNumbers(formTelefone.telefone),
        };

        if (
            clienteFinal.nome &&
            clienteFinal.telefone &&
            checked
        ) {

            setData((prev) => ({
                ...prev,
                cliente: clienteFinal,
            }));

            navigate("/Checkout/Etapa2", {
                state: {
                    cliente: clienteFinal,
                },
            });
        } else {
            alert("Por favor, preencha todos os campos obrigatórios.");
            return;
        }
    };

    return (
        <>
            <div className="Formulario-Cliente">
                <form>
                    {/* Campos de Dados Pessoais */}
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="name"><label style={{"color": "red"}}>* </label>Nome Completo:</label>
                        <input className="Entrada-Formulario"
                        ref={(el) => (refs.current[0] = el)}
                        enterKeyHint="next"
                         type="text"
                          id="nome"
                           name="nome"
                            value={data.cliente.nome}
                             onChange={handleChangeClient}
                             onKeyDown={(e) => {
                                if (e.key === "Enter") {
                                    e.preventDefault();
                                    focusNextInput(0);
                                }
                             }}
                              required
                              />
                    </div>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="telefone"><label style={{"color": "red"}}>* </label>Telefone:</label>
                        <input className="Entrada-Formulario"// <-- Handler específico para a máscara
                            type="tel" id="telefone" name="telefone" value={formTelefone.telefone} onChange={handleTelefoneChange}  required inputMode="numeric" 
                            maxLength="15"
                            ref={(el) => (refs.current[1] = el)}
                            enterKeyHint="next"
                            onKeyDown={(e) => {
                                if (e.key === "Enter") {
                                    e.preventDefault();
                                    focusNextInput(1);
                                }
                            }}
                        />
                    </div>
                    <div className="Grupo-Formulario">
                        <label className="Names-Formulario" htmlFor="email">E-mail:(opcional)</label>
                        <input 
                        className="Entrada-Formulario"
                         type="email" 
                         id="email" 
                         name="email" 
                         value={data.cliente.email} 
                         onChange={handleChangeClient} 
                         ref={(el) => (refs.current[2] = el)}
                         enterKeyHint="next"
                         onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                e.preventDefault();
                                focusNextInput(2);
                            }
                         }}
                         />
                    </div>
                    <div className="Grupo-Formulario-2">
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="cpf">Cpf: (opcional)</label>
                            <input
                             className="Entrada-Formulario"
                              type="text"
                               id="cpf"
                                name="cpf"
                                 value={data.cliente.cpf}
                                  onChange={handleChangeClient}
                                  ref={(el) => (refs.current[3] = el)}
                                  enterKeyHint="next"
                                  onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(3);}}} />
                        </div>
                        <div className="Grupo-Formulario">
                            <label className="Names-Formulario" htmlFor="observacoes">Observações: (opcional)</label>
                            <textarea
                                className="Entrada-Formulario-Observacoes" 
                                type="text" 
                                id="observacoes"
                                name="observacoes" 
                                value={data.observacoes}
                                onChange={handleChangeClient}
                                ref={(el) => (refs.current[4] = el)}
                                enterKeyHint="next"
                                onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(4);}}}                             
                             />
                        </div>
                    </div>
                    <div className="checkbox-wrapper-33">
                        <label className="checkbox">
                            <input className="checkbox__trigger visuallyhidden" 
                            type="checkbox"
                            checked={checked}
                            onChange={(e) => setChecked(e.target.checked)}
                            ref={(el) => (refs.current[5] = el)}
                            enterKeyHint="next"
                            onKeyDown={(e) => {if (e.key === "Enter") {e.preventDefault(); focusNextInput(5);}}}                            
                            required />
                            <span className="checkbox__symbol">
                            <svg
                                aria-hidden="true"
                                className="icon-checkbox"

                                width="28px"
                                height="28px"
                                viewBox="0 0 28 28"
                                version="1"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path d="M4 14l8 7L24 7"></path>
                            </svg>
                            </span>
                            <p className="checkbox__textwrapper">Ao continuar, você concorda em fornecer seus dados pessoais. <label style={{"color": "red"}}>* </label></p>
                        </label>
                    </div>
                </form>
                {/* Botões */}
                <div className="Botoes-Checkout">
                    <Link to="/">
                        <ButtonBack/>
                    </Link>
                    <ButtonNext handledSubmit={handledSubmit}/>
                </div>
            </div>
        </>
    )

}

export default FormularioCliente;