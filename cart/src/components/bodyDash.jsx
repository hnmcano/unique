import { ChevronDown, ArrowDown } from "lucide-react";
import { useState } from "react";

const accordions = [
  {
    title: "Informações do Sistema",
    content: "Detalhes sobre versão, configurações e status do sistema.",
  },
  {
    title: "Informações do Estabelecimento",
    content: "Nome, endereço, CNPJ e dados do estabelecimento.",
  },
  {
    title: "Informações do Usuário",
    content: "Perfil, permissões e preferências do usuário logado.",
  },
  {
    title: "Informações da Conta",
    content: "Plano, faturamento e dados da conta.",
  },
];

function Accordion({ title, content }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="w-full border border-solid border-foreground rounded-lg overflow-hidden hover:border-primary transition-colors">
      <button
        onClick={() => setOpen(!open)}
        className="flex w-full p-4 justify-between items-center text-left"
      >
        <span>{title}</span>
        <ChevronDown
          className="transition-transform duration-300"
          style={{ transform: open ? "rotate(180deg)" : "rotate(0deg)" }}
        />
      </button>
      <div
        className="overflow-hidden transition-all duration-300"
        style={{ maxHeight: open ? "200px" : "0px" }}
      >
        <div className="px-4 pb-4 text-sm text-muted-foreground">
          {content}
        </div>
      </div>
    </div>
  );
}

export default function BodyDash() {
  return (
    <div className="flex flex-col justify-between min-w-full h-full p-4">
      <nav className="flex items-center justify-between min-w-full flex-col">
        <div className="container flex items-center p-2 gap-2 justify-between min-w-full">
          <span className="p-3">Download arquivo .exe</span>
          <button className="flex flex-row border border-primary rounded-lg hover:bg-primary">
            <span className="p-3"><ArrowDown size={20} /></span>
            <span className="p-3">Download .exe</span>
          </button>
        </div>
        <div className="flex flex-col w-full p-14 justify-between gap-4">
          {accordions.map((item) => (
            <Accordion key={item.title} title={item.title} content={item.content} />
          ))}
        </div>
      </nav>
    </div>
  );
}