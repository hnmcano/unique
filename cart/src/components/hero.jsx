// hero.jsx
import { Button } from "@/components/ui/button"
import { ArrowRight, Play } from "lucide-react"

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-secondary py-20 md:py-32">
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]" />

      <div className="container relative px-4">
        <div className="mx-auto max-w-4xl text-center">
          <div className="mb-8 inline-block rounded-full bg-primary/10 px-4 py-1.5 text-sm font-medium text-primary">
            🚀 A solução completa para seu negócio
          </div>

          <h1 className="mb-6 text-balance text-4xl font-bold tracking-tight text-secondary-foreground sm:text-5xl md:text-6xl lg:text-7xl">
            {"O sistema de PDV e Delivery que "}
            <span className="text-primary">revoluciona</span>
            {" seu negócio"}
          </h1>

          <p className="mb-10 text-pretty text-lg text-secondary-foreground/80 sm:text-xl md:text-2xl">
            Gerencie vendas, estoque, pedidos de delivery e muito mais em uma única plataforma. Aumente suas vendas e
            simplifique sua operação.
          </p>

          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Button
              size="lg"
              className="h-12 bg-primary px-8 text-base font-semibold text-primary-foreground hover:bg-primary/90"
            >
              Começar Grátis por 14 dias
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            <Button size="lg" variant="outline" className="h-12 px-8 text-base font-semibold bg-transparent">
              <Play className="mr-2 h-5 w-5" />
              Ver Demonstração
            </Button>
          </div>

          <p className="mt-6 text-sm text-secondary-foreground/60">
            Sem cartão de crédito • Cancele quando quiser • Suporte em português
          </p>
        </div>
      </div>
    </section>
  )
}