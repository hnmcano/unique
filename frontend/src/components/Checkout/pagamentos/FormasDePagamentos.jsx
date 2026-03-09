import { useCheckout } from "../../../contexts/CheckoutContext";
import { IoIosCopy } from "react-icons/io";
import { useState } from "react";

export function PagamentoPix() {
    const {opcoesDisponiveis, SelecionarBandeira} = useCheckout();
    const chavePix = "14991231554";

    const copiarChave = async () => {
    try {
        await navigator.clipboard.writeText(chavePix);
        alert("Chave PIX copiada!");
    } catch (err) {
        console.error("Erro ao copiar:", err);
    }
};

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["pix"] ? "bandeira-metodo-pix" : "oculto"}>
                <div className="metodo-pagamento-pix">
                    <label className="descricao-pix">Para realizar o pagamento, copie a chave PIX abaixo.</label>
                    <div className="chave-pix">
                        <div className="opcao-copy-pix">
                            <input defaultValue="14991231554" placeholder="Chave PIX"/>
                        </div>
                        <IoIosCopy className="chave-pix-copy" onClick={copiarChave} />
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}


export function PagamentoCredito() {
    const {opcoesDisponiveis, SelecionarBandeira} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["credito"]  ? "bandeira-metodo-cartoes" : "oculto"}>
                <div className="metodo-pagamento-cartoes">
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("VISA")}>
                        VISA
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("MASTERCARD")}>
                        MASTERCARD
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("ELO")}>
                        ELO
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("HIPERCARD")}>
                        HIPERCARD
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export function PagamentoDebito() {
    const {opcoesDisponiveis, SelecionarBandeira} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["debito"] ? "bandeira-metodo-cartoes" : "oculto"}>
                <div className="metodo-pagamento-cartoes">
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("VISA")}>
                        VISA
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("MASTERCARD")}>
                        MASTERCARD
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("ELO")}>
                        ELO
                    </div>
                    <div className="bandeiras-cartoes" onClick={() => SelecionarBandeira("HIPERCARD")}>
                        HIPERCARD
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}


export function PagamentoDinheiro() {
    const {opcoesDisponiveis, SelecionarBandeira} = useCheckout();
    const [value, setValue] = useState(null);
    const [troco, setTroco] = useState(false);

    return (
        <>
            <div className={opcoesDisponiveis["dinheiro"] ? "bandeira-metodo-dinheiro" : "oculto"}>
                <div className="metodo-pagamento-dinheiro">
                    <div className="bandeiras-dinheiro">
                        <label className="descricao-dinheiro">Há necessidade de troco?</label>
                        <div className="botoes-radio">
                            <label> 
                                <input type="radio" name="troco" value="sim" onClick={() => setTroco(true)}/> SIM 
                            </label>
                            <label>
                                <input type="radio" name="troco" value="nao" onClick={() => setTroco(false)} onChange={(e) => SelecionarBandeira("Sem Troco")}/> NÃO
                            </label>
                        </div>
                        {troco === true && (
                            <div className="valor-troco">
                                <label className="descricao-dinheiro">Qual seria o valor (Que será entregue) ?</label>
                                <div className="valor-dinheiro">
                                    <div className="dinheiro-input-container">
                                        <input className="input-valor-dinheiro" type="text" placeholder="Valor em dinheiro" onChange={(e) => SelecionarBandeira(e.target.value)}/>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div>
        </>
    )
}
