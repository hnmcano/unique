import { Button } from "@/components/ui/button"
import { ArrowRight } from "lucide-react"

export function CTA() {
  return (
    <section className="bg-secondary py-20 md:py-32">
      <div className="container px-4">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="mb-6 text-balance text-3xl font-bold tracking-tight text-secondary-foreground sm:text-4xl md:text-5xl">
            Pronto para revolucionar seu negócio?
          </h2>
          <p className="mb-10 text-pretty text-lg text-secondary-foreground/80 md:text-xl">
            Junte-se a centenas de empresas que já aumentaram suas vendas e simplificaram suas operações com o PDV Pro.
          </p>
          <div className="flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Button
              size="lg"
              className="h-14 bg-primary px-10 text-lg font-semibold text-primary-foreground hover:bg-primary/90"
            >
              Começar Teste Grátis
              <ArrowRight className="ml-2 h-5 w-5" />
            </Button>
            <Button size="lg" variant="outline" className="h-14 px-10 text-lg font-semibold bg-transparent">
              Falar com Especialista
            </Button>
          </div>
          <p className="mt-6 text-sm text-secondary-foreground/60">
            ⚡ Configuração em 5 minutos • 💳 Sem cartão de crédito
          </p>
        </div>
      </div>
    </section>
  )
}
