import { ShoppingCart, Package, TrendingUp, Smartphone, BarChart3, Zap } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"

export function Features() {
  const features = [
    {
      icon: ShoppingCart,
      title: "PDV Completo",
      description:
        "Sistema de ponto de venda rápido e intuitivo. Processe vendas em segundos com interface otimizada para alta demanda.",
    },
    {
      icon: Smartphone,
      title: "Gestão de Delivery",
      description:
        "Gerencie pedidos de delivery integrado com os principais apps. Acompanhe entregas em tempo real e otimize rotas.",
    },
    {
      icon: Package,
      title: "Controle de Estoque",
      description:
        "Monitore seu estoque em tempo real. Alertas automáticos de produtos em falta e relatórios de giro de estoque.",
    },
    {
      icon: BarChart3,
      title: "Relatórios Avançados",
      description:
        "Dashboards inteligentes com insights sobre vendas, produtos mais vendidos e performance do seu negócio.",
    },
    {
      icon: TrendingUp,
      title: "Análise de Vendas",
      description:
        "Entenda o comportamento dos seus clientes. Identifique tendências e tome decisões baseadas em dados reais.",
    },
    {
      icon: Zap,
      title: "Integração Total",
      description:
        "Conecte com impressoras fiscais, balanças, iFood, Rappi e muito mais. Tudo sincronizado automaticamente.",
    },
  ]

  return (
    <section id="recursos" className="bg-background py-20 md:py-32">
      <div className="container px-4">
        <div className="mb-16 text-center">
          <h2 className="mb-4 text-balance text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl">
            Tudo que você precisa em um só lugar
          </h2>
          <p className="mx-auto max-w-2xl text-pretty text-lg text-muted-foreground">
            Recursos desenvolvidos especialmente para restaurantes, lanchonetes e comércios que querem crescer
          </p>
        </div>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((feature, index) => {
            const Icon = feature.icon
            return (
              <Card key={index} className="group border-2 transition-all hover:border-primary hover:shadow-lg">
                <CardContent className="p-6">
                  <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10 text-primary transition-colors group-hover:bg-primary group-hover:text-primary-foreground">
                    <Icon className="h-6 w-6" />
                  </div>
                  <h3 className="mb-2 text-xl font-bold text-foreground">{feature.title}</h3>
                  <p className="text-pretty text-muted-foreground leading-relaxed">{feature.description}</p>
                </CardContent>
              </Card>
            )
          })}
        </div>
      </div>
    </section>
  )
}
