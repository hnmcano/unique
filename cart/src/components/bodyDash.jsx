import { ChevronDown, ArrowDown, Download } from "lucide-react";
import { useState } from "react";
import { useData } from "../Context/ContextData";

function formatCNPJ(doc) {
  if (!doc) return "-";
  return doc.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");
}

function formatTelefone(tel) {
  if (!tel) return "-";
  return tel.replace(/(\d{2})(\d{5})(\d{4})/, "($1) $2-$3");
}

function formatData(iso) {
  if (!iso) return "-";
  return new Date(iso).toLocaleDateString("pt-BR");
}

function Accordion({ title, children, cor }) {
  const [open, setOpen] = useState(false);


  return (
    <div
      className="w-full rounded-xl overflow-hidden transition-colors"
      style={{
        border: open
          ? `0.5px solid ${cor}60`
          : "0.5px solid var(--color-border-tertiary)",
        background: "var(--color-background-primary)",
      }}
    >
      <button
        onClick={() => setOpen(!open)}
        className="flex w-full px-4 py-3.5 justify-between items-center text-left border-b border-border/30"
      >
        <div className="flex items-center gap-2.5">
          <div
            className="w-2 h-2 rounded-full flex-shrink-0"
            style={{ background: cor }}
          />
          <span className="text-sm font-medium">{title}</span>
        </div>
        <ChevronDown
          size={16}
          className="text-muted-foreground transition-transform duration-300"
          style={{ transform: open ? "rotate(180deg)" : "rotate(0deg)" }}
        />
      </button>

      <div
        className="overflow-hidden transition-all duration-300"
        style={{ maxHeight: open ? "400px" : "0px" }}
      >
        <div className="px-4 pb-4 pl-9 flex flex-col gap-0">
          {children}
        </div>
      </div>
    </div>
  );
}

function Row({ label, value, badge }) {
  return (
    <div className="flex justify-between items-baseline py-1.5 border-b border-border/30 last:border-none">
      <span className="text-xs text-muted-foreground">{label}</span>
      {badge ? (
        <span
          className="text-[11px] font-medium px-2 py-0.5 rounded-full"
          style={{ background: "#ffffff15", color: "#e52c29" }}
        >
          {value}
        </span>
      ) : (
        <span className="text-xs font-medium">{value ?? "-"}</span>
      )}
    </div>
  );
}

export default function BodyDash() {
  const { data, executavel } = useData();
  const est = data?.estabelecimento;
  const usuario = data?.usuario;
  const cor = est?.cor_layout ?? "#e52c29";

  function handleDownload() {
      const a = document.createElement('a');
      a.href = executavel.url;
      a.download = 'unique.exe'; // ✅ força download com nome certo
      a.click();
  }


  return (
    <div className="flex flex-col min-w-full h-full p-4">

      {/* barra superior */}
      <div className="flex items-center justify-between px-2 py-3 mb-6">
        <span className="text-sm text-muted-foreground">Painel de configurações</span>
        <button
          className="flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-opacity hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
          style={{ 
            background: executavel.loading || !executavel.url ? '#9CA3AF' : cor // ← Cinza quando desabilitado
          }}
          disabled={executavel.loading || !executavel.url}
          onClick={handleDownload}
        >
          {executavel.loading ? "Preparando..." : executavel.url ? "Download .exe" : "Carregando..."} {/* ← Só mostra Download quando tiver URL */}
        </button>
      </div>

      {/* acordeões */}
      <div className="flex flex-col gap-3 w-[90%] mx-auto">

        <Accordion title="Informações do Sistema" cor={cor}>
          <Row label="Plano" value={est?.plano} badge />
          <Row label="Subdomínio" value={est?.subdominio} />
          <Row label="Redirecionamento" value={est?.redirecionamento} />
          <Row label="Limite de usuários" value={est?.limite_usuarios} />
          <Row label="Status" value={est?.ativo ? "ativo" : "inativo"} badge />
        </Accordion>

        <Accordion title="Informações do Estabelecimento" cor={cor}>
          <Row label="Nome fantasia" value={est?.nome_fantasia} />
          <Row label="CNPJ" value={formatCNPJ(est?.documento)} />
          <Row label="Email" value={est?.email} />
          <Row label="Telefone" value={formatTelefone(est?.telefone)} />
          <Row label="Endereço" value={est?.endereco} />
          <Row label="Rede social" value={est?.rede_social ? `@${est.rede_social}` : "-"} />
          <Row label="Descrição" value={est?.descricao} />
        </Accordion>

        <Accordion title="Informações do Usuário" cor={cor}>
          <Row label="Nome" value={usuario?.nome} />
          <Row label="Email" value={usuario?.email} />
          <Row label="Status" value={usuario?.ativo ? "ativo" : "inativo"} badge />
          <Row label="Criado em" value={formatData(usuario?.criado_em)} />
        </Accordion>

        <Accordion title="Informações da Conta" cor={cor}>
          <Row label="Plano atual" value={est?.plano} badge />
          <Row label="Expiração" value={formatData(est?.data_expiracao) ?? "sem expiração"} />
          <Row label="Cor do layout" value={est?.cor_layout} />
          <Row label="Criado em" value={formatData(est?.criado_em)} />
          <Row label="Atualizado em" value={formatData(est?.atualizado_em)} />
        </Accordion>

      </div>
    </div>
  );
}