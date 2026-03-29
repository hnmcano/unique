import { Card, CardContent } from "@/components/ui/card"
import { Star } from "lucide-react"

export function Testimonials() {
  const testimonials = [
    {
      name: "Carlos Silva",
      role: "Dono - Restaurante Sabor Caseiro",
      content:
        "Antes do PDV Pro, perdíamos muito tempo no fechamento do caixa. Agora tudo é automático e rápido. Recomendo!",
      rating: 5,
    },
    {
      name: "Ana Paula Costa",
      role: "Gerente - Lanchonete da Praça",
      content:
        "A integração com os apps de delivery foi um divisor de águas. Centralizamos tudo e aumentamos nossas vendas em 300%.",
      rating: 5,
    },
    {
      name: "Roberto Mendes",
      role: "Proprietário - Pizzaria Napolitana",
      content:
        "O suporte é excepcional e o sistema nunca falha. Nosso atendimento ficou 6x mais rápido. Melhor investimento que fizemos!",
      rating: 5,
    },
  ]

  return (
    <section id="depoimentos" className="bg-muted py-20 md:py-32">
      <div className="container px-4">
        <div className="mb-16 text-center">
          <h2 className="mb-4 text-balance text-3xl font-bold tracking-tight text-foreground sm:text-4xl md:text-5xl">
            Quem usa, aprova
          </h2>
          <p className="mx-auto max-w-2xl text-pretty text-lg text-muted-foreground">
            Veja o que nossos clientes dizem sobre o PDV Pro
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {testimonials.map((testimonial, index) => (
            <Card key={index} className="bg-card">
              <CardContent className="p-6">
                <div className="mb-4 flex gap-1">
                  {Array.from({ length: testimonial.rating }).map((_, i) => (
                    <Star key={i} className="h-5 w-5 fill-primary text-primary" />
                  ))}
                </div>
                <p className="mb-6 text-pretty text-card-foreground leading-relaxed">{testimonial.content}</p>
                <div>
                  <div className="font-semibold text-foreground">{testimonial.name}</div>
                  <div className="text-sm text-muted-foreground">{testimonial.role}</div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
