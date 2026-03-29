import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Check } from "lucide-react"

export function Pricing() {
  const plans = [
    {
      name: "Starter",
      price: "R$ 97",
      description: "Perfeito para pequenos negócios começando",
      features: [
        "1 Caixa PDV",
        "Gestão de Delivery",
        "Controle de Estoque Básico",
        "Relatórios Essenciais",
        "Suporte por Email",
        "Até 1.000 vendas/mês",
      ],
      highlighted: false,
    },
    {
      name: "Professional",
      price: "R$ 197",
      description: "Para negócios em crescimento",
      features: [
        "Até 3 Caixas PDV",
        "Gestão Avançada de Delivery",
        "Controle de Estoque Completo",
        "Relatórios e Dashboards",
        "Suporte Prioritário",
        "Vendas Ilimitadas",
        "Integração com Apps",
        "Gestão de Funcionários",
      ],
      highlighted: true,
    },
    {
      name: "Enterprise",
      price: "R$ 397",
      description: "Para operações de grande porte",
      features: [
        "Caixas PDV Ilimitados",
        "Multi-lojas",
        "Controle Avançado de Estoque",
        "Business Intelligence",
        "Suporte 24/7 com WhatsApp",
        "Vendas Ilimitadas",
        "Todas as Integrações",
        "Treinamento Personalizado",
        "API Customizada",
      ],
      highlighted: false,
    },
  ]

  return (
    <section id="precos" className="bg-background py-20 md:py-32">
      <div className="container px-4">
        <div className="mb-16 text-center">
          <h2 className="mb-4 text-balance text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl">
            Planos que cabem no seu bolso
          </h2>
          <p className="mx-auto max-w-2xl text-pretty text-lg text-muted-foreground">
            Escolha o plano ideal para o seu negócio. Teste grátis por 14 dias, sem compromisso.
          </p>
        </div>

        <div className="grid gap-8 lg:grid-cols-3">
          {plans.map((plan, index) => (
            <Card key={index} className={plan.highlighted ? "border-2 border-primary shadow-xl" : "border-2"}>
              <CardHeader>
                {plan.highlighted && (
                  <div className="mb-2 inline-block w-fit rounded-full bg-primary px-3 py-1 text-xs font-semibold text-primary-foreground">
                    Mais Popular
                  </div>
                )}
                <CardTitle className="text-2xl">{plan.name}</CardTitle>
                <CardDescription className="text-pretty">{plan.description}</CardDescription>
                <div className="mt-4">
                  <span className="text-4xl font-bold text-foreground">{plan.price}</span>
                  <span className="text-muted-foreground">/mês</span>
                </div>
              </CardHeader>
              <CardContent>
                <ul className="space-y-3">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-start gap-3">
                      <Check className="h-5 w-5 shrink-0 text-primary" />
                      <span className="text-sm text-card-foreground">{feature}</span>
                    </li>
                  ))}
                </ul>
              </CardContent>
              <CardFooter>
                <Button className="w-full" variant={plan.highlighted ? "default" : "outline"} size="lg">
                  {plan.highlighted ? "Começar Agora" : "Escolher Plano"}
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>

        <p className="mt-12 text-center text-sm text-muted-foreground">
          Todos os planos incluem 14 dias grátis • Cancele quando quiser • Migração gratuita
        </p>
      </div>
    </section>
  )
}
