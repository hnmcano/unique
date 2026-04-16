import { useCheckout } from "../../contexts/CheckoutContext";
import { useNavigate } from "react-router-dom";
import { useStatus } from "../../contexts/StatusContext";
import { Link } from "react-router-dom";
import api from "../../api/api";
import { PagamentoCredito, PagamentoDebito, PagamentoDinheiro, PagamentoPix } from "./pagamentos/FormasDePagamentos";
import { useEstabelecimento } from "../../contexts/EstabelecimentoContext";
import { IconePix, IconeCredito, IconeDebito, IconeDinheiro } from "./pagamentos/iconesSvg";
import { ButtonBack } from "./buttons/ButtonsCheckout";
import { useState, useMemo } from "react";
import { MdOutlineCancel } from "react-icons/md";
import { useProdutos } from "../../hooks/useProdutos";
import "../../styles/Enviar.css";
import { useCarrinho } from "../../contexts/CarrinhoContext";

function FormasPagPedido() {
    const { data, valor_total, SelecionarMetodo, opcoesDisponiveis, formaPagamento } = useCheckout();
    const { base } = useProdutos();
    const { produtos: produtosCarrinho } = useCarrinho();
    const { atualizarPedido } = useStatus();
    const { estabelecimento } = useEstabelecimento();

    const [isLoading, setIsLoading] = useState(false);
    const [isSuccess, setIsSuccess] = useState(false);
    const [error, setError] = useState(null);
    const [respostaServidor, setRespostaServidor] = useState(null);

    const navigate = useNavigate();

    // ✅ DADOS DO PEDIDO (100% corretos vindos do carrinho)
    const prepararDadosPedido = (dataPedido) => {
        const itensFormatados = produtosCarrinho.map((p) => ({
            produto_id: p.produto_id,
            quantidade: p.quantidade,
            valor_unitario: p.preco_venda,
            valor_total: p.quantidade * p.preco_venda,
            tamanho: p.tamanho || "",
        }));

        return {
            ...dataPedido,
            itens: itensFormatados
        };
    };

    const dadosPedidoPronto = useMemo(
        () => prepararDadosPedido(data),
        [data, produtosCarrinho]
    );

    // ✅ AGRUPAR ITENS PARA WHATSAPP
    const agruparItens = (itens) => {
        const mapa = {};

        itens.forEach(item => {
            const nome = item.tamanho
                ? `${item.nome || "Produto"} (${item.tamanho})`
                : item.nome || "Produto";

            if (!mapa[nome]) {
                mapa[nome] = {
                    ...item,
                    quantidade: 0
                };
            }

            mapa[nome].quantidade += item.quantidade;
        });

        return Object.values(mapa);
    };

    // ✅ WHATSAPP
    const enviarPedidoWhatsApp = () => {
        if (!estabelecimento?.telefone) {
            alert("Telefone do estabelecimento não encontrado");
            return;
        }

        const produtosMap = {};
        base.forEach(categoria => {
            categoria.produtos.forEach(produto => {
                produtosMap[produto.id] = produto;
            });
        });

        const mensagem = [
            "🧾 Pedido - " + estabelecimento.nome,
            "",
            "👤 Cliente: " + (data.cliente?.nome || "Não informado"),
            "📞 Telefone: " + (data.cliente?.telefone || "Não informado"),
            "",
            "📍 Endereço: " + (data.entrega?.endereco + " " + data.entrega?.numero || ""),
            "📍 Bairro: " + (data.entrega?.bairro || ""),
            "📍 Cidade: " + (data.entrega?.cidade || ""),
            "",
            "💰 Pagamento: " + (data.metodo_pagamento || ""),
            "",
            "📦 Itens:",
            ...agruparItens(dadosPedidoPronto.itens).map((item) => {
                const produto = produtosMap[item.produto_id];
                const nomeProduto = produto ? produto.nome : "Produto";

                const totalItem = item.quantidade * Number(item.valor_unitario || 0);

                return `- ${item.quantidade}x ${nomeProduto}${item.tamanho ? ` (${item.tamanho})` : ""} - R$ ${totalItem.toFixed(2)}`;
            }),
            "",
            "🚚 Taxa: R$ " + (data.entrega?.taxa_entrega?.toFixed(2) || "0.00"),
            "💰 Total: R$ " + (data.valor_total?.toFixed(2) || "0.00")
        ].join("\n");

        const url = `https://api.whatsapp.com/send?phone=${estabelecimento.telefone}&text=${encodeURIComponent(mensagem)}`;
        window.open(url, "_blank");
    };

    // ✅ ENVIO
    const handledSubmit = async (event) => {
        event.preventDefault();
        if (isLoading) return;

        setIsLoading(true);
        setIsSuccess(false);

        try {
            const dados_estabelecimento = await api.get(`/estabelecimento/carregar-dados`);

            if (dados_estabelecimento.data.redirecionamento === "unique") {
                const response = await api.post("/pedidos/react", dadosPedidoPronto);

                setIsLoading(false);
                setIsSuccess(true);

                setTimeout(() => {
                    atualizarPedido(response.data);
                    navigate(`/Status/Pedido/${response.data.id_pedido}`);
                }, 2000);

            } else {
                enviarPedidoWhatsApp();
                setIsLoading(false);
                setIsSuccess(true);
            }

        } catch (error) {
            console.log(error);
            setIsLoading(false);
            setError(error);
            setRespostaServidor(error?.response?.data?.detail || "Erro ao enviar pedido");
        }
    };

    if (respostaServidor) {
        return (
            <div className="resposta-servidor-container">
                <MdOutlineCancel className="resposta-servidor-icon" />
                <p>{respostaServidor}</p>
                <Link to="/">
                    <ButtonBack />
                </Link>
            </div>
        );
    }
    
    return (
        <>
        {isLoading && <div className="fullscreen-loading" />}
            <div className="metodos-pagamento-container">
                <div className="formas-pagamentos">
                    <div className="opcao-pagamento" >
                        <label className={data.metodo_pagamento === "pix" ? "checkbox-pagamentos-ativo" : "checkbox-pagamentos"} onClick={() => SelecionarMetodo("pix")} >
                            <IconePix onClick={() => SelecionarMetodo("pix")}/>
                            <span className="label-checkbox-pagamentos" onClick={() => SelecionarMetodo("pix")}>PIX</span>
                            <input
                                type="radio"
                                name="pagamento"
                                value="pix"
                                style={{ display: "none"}}
                                checked={formaPagamento === "pix"}
                            />
                        </label>
                        {opcoesDisponiveis === "pix" && (<PagamentoPix />)}
                    </div>
                    <div className="opcao-pagamento" >
                        <label className={data.metodo_pagamento === "credito" ? "checkbox-pagamentos-ativo" : "checkbox-pagamentos"} onClick={() => SelecionarMetodo("credito")}>
                            <IconeCredito onClick={() => SelecionarMetodo("credito")}/>
                            <span className="label-checkbox-pagamentos" onClick={() => SelecionarMetodo("credito")}>CRÉDITO</span>
                            <input
                                type="radio"
                                name="pagamento"
                                value="credito"
                                style={{ display: "none"}}
                                checked={formaPagamento === "credito"}
                            />
                        </label>
                        {opcoesDisponiveis === "credito" && (<PagamentoCredito />)}
                    </div>
                    <div className="opcao-pagamento" >
                        <label className={data.metodo_pagamento === "debito" ? "checkbox-pagamentos-ativo" : "checkbox-pagamentos"} onClick={() => SelecionarMetodo("debito")}>
                            <IconeDebito onClick={() => SelecionarMetodo("debito")} />
                            <span className="label-checkbox-pagamentos" onClick={() => SelecionarMetodo("debito")}>DÉBITO</span>
                            <input
                                type="radio"
                                name="pagamento"
                                value="debito"
                                style={{ display: "none"}}
                                checked={formaPagamento === "debito"}
                            />
                        </label>
                        {opcoesDisponiveis === "debito" && (<PagamentoDebito />)}
                    </div>
                    <div className="opcao-pagamento" >
                        <label className={data.metodo_pagamento === "dinheiro" ? "checkbox-pagamentos-ativo" : "checkbox-pagamentos"} onClick={() => SelecionarMetodo("dinheiro")}>
                            <IconeDinheiro onClick={() => SelecionarMetodo("dinheiro")}/>
                            <span className="label-checkbox-pagamentos" onClick={() => SelecionarMetodo("dinheiro")}>DINHEIRO</span>
                            <input
                                type="radio"
                                name="pagamento"
                                value="dinheiro"
                                style={{ display: "none"}}
                                checked={formaPagamento === "dinheiro"}
                            />
                        </label>
                        {opcoesDisponiveis === "dinheiro" && (<PagamentoDinheiro />)}
                    </div>
                </div>
                <div style={{"width":"100%"}}>
                    <div className="container-total-geral" style={{marginBottom: "20px"}}>
                        <h3 style={{"color": "white"}}>TOTAL GERAL</h3>
                        <h3 className="value-total-geral"><label>R${valor_total.toFixed(2)}</label></h3>
                    </div>
                    <div className="Botoes-Checkout">
                        <Link to="/Checkout/Etapa3">
                            <ButtonBack/>
                        </Link>
                        <button
                            onClick={handledSubmit}
                            className={`send 
                                ${isLoading ? "is-loading" : ""} 
                                ${isSuccess ? "is-success" : ""}
                                ${error ? "is-error" : ""}
                            `}
                        >
                            <svg viewBox="0 0 90.594 59.714">
                                <polyline
                                    className="check"
                                    fill="none"
                                    stroke="#FFFFFF"
                                    strokeWidth="10"
                                    strokeMiterlimit="10"
                                    points="1.768,23.532 34.415,56.179 88.826,1.768"
                                />  
                            </svg>
                            <span>Send</span>
                        </button>
                    </div>
                </div>
            </div>
        </>
    )

}


export default FormasPagPedido;
