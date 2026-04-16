// HelpTutorial.jsx
import { useState } from "react";
import { 
  Utensils, 
  Search, 
  Rocket, 
  Package, 
  Armchair, 
  Bike, 
  Calculator, 
  Settings, 
  ChevronDown, 
  Mail, 
  Phone, 
  MessageCircle, 
  HelpCircle,
  BookOpen,
  Play,
  Download,
  CheckCircle2,
  AlertCircle,
  Info
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

// Dados dos tutoriais baseados no seu sistema UNIQUE
const tutoriais = [
  {
    id: "primeiros-passos",
    titulo: "Primeiros Passos",
    icon: Rocket,
    cor: "text-primary",
    steps: [
      { titulo: "Login Inicial", desc: "Use seu e-mail e senha cadastrados. O sistema salva seu login automaticamente." },
      { titulo: "Verificação de Caixa", desc: "Ao abrir, o sistema verifica se o caixa está aberto. Se estiver fechado, vá em Caixa Registradora primeiro." },
      { titulo: "Status de Conexão", desc: "Observe o ícone 🟢 Conectado no canto inferior. Se aparecer 🔴, verifique sua internet." }
    ],
    alerta: { tipo: "warning", texto: "Importante: Sempre abra o caixa antes de fazer vendas ou receber pedidos delivery." }
  },
  {
    id: "produtos",
    titulo: "Cadastro de Produtos",
    icon: Package,
    cor: "text-primary",
    steps: [
      { titulo: "Acesse o Módulo", desc: "Clique em Produtos no menu principal ou no ícone correspondente." },
      { titulo: "Adicionar Novo", desc: "Clique no botão + vermelho. Preencha: Nome, Código PDV, Preços (custo/venda) e Estoque." },
      { titulo: "Foto do Produto", desc: "Clique em 'Selecionar Imagem' para adicionar foto. Formatos: PNG, JPG." },
      { titulo: "Categorias", desc: "Use o botão + Categoria para criar grupos (Bebidas, Lanches, etc)." }
    ],
    alerta: { tipo: "info", texto: "Dica: Produtos com estoque baixo aparecem destacados no PDV." }
  },
  {
    id: "mesas",
    titulo: "Controle de Mesas",
    icon: Armchair,
    cor: "text-primary",
    steps: [
      { titulo: "Abrir Mesa", desc: "Clique no botão Mesas no menu. Escolha uma mesa livre (botão sem borda verde)." },
      { titulo: "Adicionar Itens", desc: "Na tela da mesa, clique em + Produtos. Selecione os itens do cardápio." },
      { titulo: "Controle de Quantidade", desc: "Use os botões + e - na tabela para ajustar quantidades." },
      { titulo: "Fechar Mesa", desc: "Clique em Finalizar para encerrar e liberar a mesa." }
    ],
    alerta: { tipo: "success", texto: "Visual: Mesas ocupadas ficam com borda verde ao redor do botão." }
  },
  {
    id: "delivery",
    titulo: "Pedidos Delivery",
    icon: Bike,
    cor: "text-primary",
    steps: [
      { titulo: "Acessar Entregas", desc: "Clique em Entregas no menu principal." },
      { titulo: "Novos Pedidos", desc: "Pedidos online aparecem automaticamente com notificação sonora e badge vermelho." },
      { titulo: "Gerenciar Status", desc: "Clique no status atual para mudar: Laranja (Pendente), Vermelho (Produção), Verde (Entrega)." },
      { titulo: "Imprimir Cupom", desc: "No detalhe do pedido, clique em Imprimir para enviar para impressora térmica." }
    ]
  },
  {
    id: "caixa",
    titulo: "Caixa Registradora",
    icon: Calculator,
    cor: "text-primary",
    steps: [
      { titulo: "Abertura", desc: "Informe o valor inicial (troco) e clique em Abrir Caixa." },
      { titulo: "Acompanhamento", desc: "Veja o valor total de vendas do dia e formas de pagamento usadas." },
      { titulo: "Fechamento", desc: "Ao final do expediente, clique em Fechar Caixa. O sistema calcula o total automaticamente." },
      { titulo: "Impressão", desc: "Use Fechar e Imprimir para gerar relatório físico do dia." }
    ],
    alerta: { tipo: "warning", texto: "Atenção: Não é possível vender com caixa fechado. O sistema exige abertura diária." }
  },
  {
    id: "configuracoes",
    titulo: "Configurações",
    icon: Settings,
    cor: "text-primary",
    steps: [
      { titulo: "Impressoras", desc: "Em Configurações > Impressoras, selecione sua impressora térmica. Use Testar para verificar." },
      { titulo: "Estabelecimento", desc: "Configure dados da loja, horários de funcionamento e cores do sistema." },
      { titulo: "Funcionários", desc: "Cadastre usuários com permissões de acesso no módulo Funcionários." }
    ]
  }
];

// Dados do FAQ baseados no seu código PySide6
const faqs = [
  {
    pergunta: "O sistema não conecta (Status: Desconectado)",
    resposta: [
      "Verifique a conexão de internet do computador",
      "Se o servidor/backend está online",
      "Reinicie o aplicativo",
      "Verifique se o token de acesso não expirou (faça logout e login novamente)"
    ]
  },
  {
    pergunta: "Não consigo cadastrar produtos (erro de BD)",
    resposta: [
      "Preço com vírgula: Use ponto (.) ou vírgula (,) - o sistema aceita ambos",
      "Código PDV duplicado: Cada produto precisa de um código único",
      "Imagem muito grande: Reduza a foto para menos de 2MB",
      "Categoria vazia: Selecione ou crie uma categoria antes de salvar"
    ]
  },
  {
    pergunta: "Impressora não imprime o cupom",
    resposta: [
      "Verifique se a impressora está ligada e com papel",
      "Em Configurações > Impressoras, clique em Testar",
      "Se não imprimir, reinstale o driver da impressora térmica",
      "Modelos compatíveis: EPSON TM-T20, Bematech MP-4200, Elgin i9",
      "O sistema usa impressão RAW Windows (win32print). Execute como Administrador se necessário."
    ]
  },
  {
    pergunta: "Pedidos delivery não aparecem na tela",
    resposta: [
      "Se o WebSocket está conectado (status verde no rodapé)",
      "Filtros ativos na tabela (limpe o campo de busca)",
      "Se os pedidos não estão com status FINALIZADO (eles somem da lista)",
      "Volume do computador (deve tocar um som ao receber)"
    ]
  },
  {
    pergunta: "Caixa fecha sozinho ou dá erro ao abrir",
    resposta: [
      "Erro 'Caixa já aberto': Só pode ter um caixa aberto por dia. Feche o anterior antes.",
      "Erro de valor: Digite apenas números no valor inicial (ex: 100.00)",
      "Perda de conexão: O caixa permanece aberto no servidor, mas a tela pode travar. Reinicie."
    ]
  },
  {
    pergunta: "Como adicionar mais mesas ao sistema?",
    resposta: [
      "No módulo Mesas, clique no botão + no canto inferior direito da grade.",
      "O sistema adiciona automaticamente 'Mesa 05', 'Mesa 06', etc.",
      "Limite técnico: O sistema suporta até 99 mesas (Mesa_01 a Mesa_99)."
    ]
  }
];

export default function HelpTutorial() {
  const [searchTerm, setSearchTerm] = useState("");
  const [openFaq, setOpenFaq] = useState(null);

  const filteredTutoriais = tutoriais.filter(t => 
    t.titulo.toLowerCase().includes(searchTerm.toLowerCase()) ||
    t.steps.some(s => s.desc.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  const filteredFaqs = faqs.filter(f => 
    f.pergunta.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'center' });
      element.classList.add('ring-2', 'ring-primary');
      setTimeout(() => element.classList.remove('ring-2', 'ring-primary'), 2000);
    }
  };

  const getAlertStyles = (tipo) => {
    switch(tipo) {
      case "warning": return "bg-yellow-500/10 border-yellow-500/20 text-yellow-400";
      case "success": return "bg-green-500/10 border-green-500/20 text-green-400";
      case "info": return "bg-blue-500/10 border-blue-500/20 text-blue-400";
      default: return "bg-muted text-muted-foreground";
    }
  };

  const getAlertIcon = (tipo) => {
    switch(tipo) {
      case "warning": return <AlertCircle className="w-4 h-4" />;
      case "success": return <CheckCircle2 className="w-4 h-4" />;
      case "info": return <Info className="w-4 h-4" />;
      default: return null;
    }
  };

  return (
    <div className="min-h-screen bg-background text-foreground">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-16 items-center justify-between px-4">
          <div className="flex items-center gap-2">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary">
              <Utensils className="h-5 w-5 text-primary-foreground" />
            </div>
            <span className="text-xl font-bold">UNIQUE</span>
          </div>
          <nav className="hidden md:flex items-center gap-6">
            <a href="#tutorial" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
              Tutorial
            </a>
            <a href="#faq" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
              Dúvidas
            </a>
            <a href="#suporte" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">
              Suporte
            </a>
          </nav>
          <div className="flex items-center gap-2">
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
            </span>
            <span className="text-xs text-muted-foreground hidden sm:inline">Sistema Online</span>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative overflow-hidden bg-secondary py-16 md:py-24">
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]" />
        
        <div className="container relative px-4">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="mb-4 text-balance text-4xl font-bold tracking-tight text-secondary-foreground sm:text-5xl md:text-6xl">
              Central de Ajuda <span className="text-primary">UNIQUE</span>
            </h1>
            <p className="mb-8 text-pretty text-lg text-secondary-foreground/80">
              Guia completo para dominar seu sistema de gestão. Do primeiro acesso ao fechamento de caixa.
            </p>
            
            {/* Search */}
            <div className="relative max-w-xl mx-auto">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
              <input 
                type="text"
                placeholder="Buscar por funcionalidade (ex: 'caixa', 'delivery', 'impressora')..."
                className="w-full rounded-full border border-input bg-background py-3 pl-10 pr-4 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>
          </div>
        </div>
      </section>

      {/* Quick Actions */}
      <section className="container px-4 -mt-8 relative z-10">
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {[
            { icon: Rocket, title: "Primeiros Passos", desc: "Configure seu caixa e abra o sistema", id: "primeiros-passos" },
            { icon: Package, title: "Cadastrar Produtos", desc: "Adicione itens ao cardápio", id: "produtos" },
            { icon: Armchair, title: "Gerenciar Mesas", desc: "Abra mesas e controle pedidos", id: "mesas" },
            { icon: Bike, title: "Delivery", desc: "Receba pedidos online", id: "delivery" }
          ].map((action, idx) => (
            <Card 
              key={idx} 
              className="cursor-pointer border-2 transition-all hover:border-primary hover:shadow-lg hover:-translate-y-1 bg-card"
              onClick={() => scrollToSection(action.id)}
            >
              <CardContent className="p-6 text-center">
                <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10 text-primary">
                  <action.icon className="h-6 w-6" />
                </div>
                <h3 className="mb-2 font-semibold text-foreground">{action.title}</h3>
                <p className="text-sm text-muted-foreground">{action.desc}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      {/* Tutorial Section */}
      <section id="tutorial" className="container px-4 py-16 md:py-24">
        <div className="mb-12 flex items-center gap-3 border-l-4 border-primary pl-4">
          <BookOpen className="h-8 w-8 text-primary" />
          <h2 className="text-3xl font-bold tracking-tight">Tutoriais por Módulo</h2>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {filteredTutoriais.map((tutorial) => (
            <Card key={tutorial.id} id={tutorial.id} className="border-2 border-border bg-card transition-all hover:border-primary/50">
              <CardHeader className="border-b border-border/50 bg-muted/50">
                <div className="flex items-center gap-3">
                  <div className={`flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 ${tutorial.cor}`}>
                    <tutorial.icon className="h-5 w-5" />
                  </div>
                  <CardTitle className="text-xl">{tutorial.titulo}</CardTitle>
                </div>
              </CardHeader>
              <CardContent className="p-6">
                <ol className="space-y-4">
                  {tutorial.steps.map((step, idx) => (
                    <li key={idx} className="flex gap-3">
                      <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-primary text-xs font-bold text-primary-foreground">
                        {idx + 1}
                      </span>
                      <div>
                        <p className="font-medium text-foreground">{step.titulo}</p>
                        <p className="text-sm text-muted-foreground leading-relaxed">{step.desc}</p>
                      </div>
                    </li>
                  ))}
                </ol>
                
                {tutorial.alerta && (
                  <div className={`mt-4 flex gap-2 rounded-lg border p-3 text-sm ${getAlertStyles(tutorial.alerta.tipo)}`}>
                    {getAlertIcon(tutorial.alerta.tipo)}
                    <p>{tutorial.alerta.texto}</p>
                  </div>
                )}
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      {/* FAQ Section */}
      <section id="faq" className="container px-4 py-16 bg-secondary/30 border-y border-border">
        <div className="mb-12 flex items-center gap-3 border-l-4 border-primary pl-4">
          <HelpCircle className="h-8 w-8 text-primary" />
          <h2 className="text-3xl font-bold tracking-tight">Perguntas Frequentes</h2>
        </div>

        <div className="mx-auto max-w-3xl space-y-4">
          {filteredFaqs.map((faq, idx) => (
            <div 
              key={idx} 
              className={`rounded-xl border bg-card overflow-hidden transition-all ${openFaq === idx ? 'border-primary/50' : 'border-border'}`}
            >
              <button 
                className="flex w-full items-center justify-between p-4 text-left hover:bg-muted/50 transition-colors"
                onClick={() => setOpenFaq(openFaq === idx ? null : idx)}
              >
                <span className="font-medium text-foreground">{faq.pergunta}</span>
                <ChevronDown 
                  className={`h-5 w-5 text-muted-foreground transition-transform ${openFaq === idx ? 'rotate-180' : ''}`} 
                />
              </button>
              
              <div 
                className="overflow-hidden transition-all"
                style={{ maxHeight: openFaq === idx ? '500px' : '0' }}
              >
                <div className="border-t border-border/50 p-4 bg-muted/20">
                  <ul className="space-y-2">
                    {faq.resposta.map((item, i) => (
                      <li key={i} className="flex gap-2 text-sm text-muted-foreground">
                        <span className="text-primary">•</span>
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Support CTA */}
      <section id="suporte" className="container px-4 py-16 md:py-24">
        <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-secondary to-background border border-border p-8 md:p-12">
          <div className="relative z-10 mx-auto max-w-2xl text-center">
            <h3 className="mb-4 text-2xl font-bold text-foreground md:text-3xl">
              Precisa de ajuda personalizada?
            </h3>
            <p className="mb-8 text-muted-foreground">
              Nossa equipe está disponível para ajudar com configurações, treinamento e resolução de problemas técnicos.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="bg-primary hover:bg-primary/90 text-primary-foreground">
                <MessageCircle className="mr-2 h-5 w-5" />
                WhatsApp Suporte
              </Button>
              <Button size="lg" variant="outline" className="border-primary text-primary hover:bg-primary/10">
                <Mail className="mr-2 h-5 w-5" />
                suporte@unique.com
              </Button>
            </div>

            <div className="mt-8 pt-6 border-t border-border/50">
              <p className="text-sm text-muted-foreground">
                Horário de Atendimento: Segunda a Sexta 08h às 20h • Sábado 09h às 14h
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer Simples */}
      <footer className="border-t border-border bg-background py-8">
        <div className="container px-4 text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <Utensils className="h-5 w-5 text-primary" />
            <span className="font-bold">UNIQUE Systems</span>
          </div>
          <p className="text-sm text-muted-foreground">
            © 2024 UNIQUE Systems. Todos os direitos reservados.
          </p>
          <p className="text-xs text-muted-foreground/60 mt-1">
            Sistema POS desenvolvido para restaurantes, bares e lanchonetes.
          </p>
        </div>
      </footer>
    </div>
  );
}
