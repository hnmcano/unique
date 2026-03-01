import { useCheckout } from "../../../contexts/CheckoutContext";
import { IoIosCopy } from "react-icons/io";

export function PagamentoPix() {
    const {opcoesDisponiveis, ToogleVisibility} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["pix"] ? "bandeira-metodo-pix" : "oculto"}>
                <div className="metodo-pagamento-pix">
                    <label className="descricao-pix">Para realizar o pagamento, copie a chave PIX abaixo.</label>
                    <div className="chave-pix">
                        <div className="opcao-copy-pix">
                            <input type="text" placeholder="Chave PIX"/>
                        </div>
                        <IoIosCopy className="chave-pix-copy" />
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}


export function PagamentoCredito() {
    const {opcoesDisponiveis, ToogleVisibility} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["credito"]  ? "bandeira-metodo-cartoes" : "oculto"}>
                <div className="metodo-pagamento-cartoes">
                    <div className="bandeiras-cartoes">
                        VISA
                    </div>
                    <div className="bandeiras-cartoes">
                        MASTERCARD
                    </div>
                    <div className="bandeiras-cartoes">
                        ELO
                    </div>
                    <div className="bandeiras-cartoes">
                        HIPERCARD
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export function PagamentoDebito() {
    const {opcoesDisponiveis, ToogleVisibility} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["debito"] ? "bandeira-metodo-cartoes" : "oculto"}>
                <div className="metodo-pagamento-cartoes">
                    <div className="bandeiras-cartoes">
                        VISA
                    </div>
                    <div className="bandeiras-cartoes">
                        MASTERCARD
                    </div>
                    <div className="bandeiras-cartoes">
                        ELO
                    </div>
                    <div className="bandeiras-cartoes">
                        HIPERCARD
                    </div>
                </div>
            </div>
        </div>
        </>
    )
}


export function PagamentoDinheiro() {
    const {opcoesDisponiveis, ToogleVisibility} = useCheckout();

    return (
        <>
        <div>
            <div className={opcoesDisponiveis["dinheiro"] ? "bandeira-metodo-dinheiro" : "oculto"}>
                DINHEIRO
            </div>
        </div>
        </>
    )
}
