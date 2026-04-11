// stats.jsx
export function Stats() {
  const stats = [
    {
      value: "50 horas",
      label: "economizadas por mês",
      company: "Restaurante Vila Nova",
    },
    {
      value: "98%",
      label: "de satisfação",
      company: "Lanchonete Express",
    },
    {
      value: "300%",
      label: "aumento em vendas",
      company: "Pizzaria Bella",
    },
    {
      value: "6x",
      label: "mais rápido no atendimento",
      company: "Hamburgueria Gourmet",
    },
  ]

  return (
    <section className="border-b border-border bg-background py-16 md:py-20">
      <div className="container px-4">
        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {stats.map((stat, index) => (
            <div key={index} className="flex flex-col border-l-4 border-primary bg-card p-6 shadow-sm">
              <div className="mb-2 text-4xl font-bold text-primary md:text-5xl">{stat.value}</div>
              <div className="mb-1 text-sm font-medium text-foreground">{stat.label}</div>
              <div className="text-xs text-muted-foreground">{stat.company}</div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}