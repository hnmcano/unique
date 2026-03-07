import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import Image from 'next/image'
import Link from 'next/link'

export default function Home() {
  return (
    <>
      <main className="min-h-screen bg-black text-white">
        {/* Header */}
        <header className="border-b border-gray-800 bg-black">
          <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <div className="h-8 w-8 rounded-full bg-blue-500"></div>
                <span className="text-xs font-semibold tracking-widest text-gray-400">UNIQUE - PDV E DELIVERY</span>
              </div>
              <nav className="hidden items-center gap-8 md:flex">
                <Link href="#features" className="text-sm text-gray-300 hover:text-white transition">Recursos</Link>
                <Link href="#why" className="text-sm text-gray-300 hover:text-white transition">Por que UNIQUE</Link>
                <Link href="#contact" className="text-sm text-gray-300 hover:text-white transition">Contato</Link>
              </nav>
            </div>
          </div>
        </header>

        {/* Hero Section */}
        <section className="relative overflow-hidden bg-black px-4 py-20 sm:px-6 lg:px-8">
          {/* Decorative elements */}
          <div className="absolute left-0 top-20 h-32 w-32 text-blue-500 opacity-20">
            <svg viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M 20 50 Q 30 30 50 20 T 80 50" />
              <path d="M 20 50 Q 30 70 50 80 T 80 50" />
            </svg>
          </div>
          <div className="absolute right-0 top-0 h-40 w-40 text-blue-400 opacity-10">
            <svg viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="2">
              <circle cx="50" cy="50" r="40" />
              <path d="M 30 50 Q 50 30 70 50" />
            </svg>
          </div>

          <div className="relative mx-auto max-w-4xl text-center">
            <h1 className="text-balance text-5xl font-bold leading-tight sm:text-6xl">
              Bem-vindo ao <br />
              <span className="text-blue-400">UNIQUE:</span> sua solução completa
            </h1>
            <Button asChild className="mt-8 bg-red-600 hover:bg-red-700 text-white">
              <Link href="#contact">EXPERIMENTE AGORA</Link>
            </Button>
          </div>
        </section>

        {/* Store Image Section */}
        <section className="px-4 py-12 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="relative h-96 w-full overflow-hidden rounded-lg">
              <Image
                src="/unique-store.jpg"
                alt="Loja UNIQUE com PDV"
                fill
                className="object-cover"
                priority
              />
            </div>
          </div>
        </section>

        {/* Como o UNIQUE transforma */}
        <section id="features" className="bg-black px-4 py-20 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="grid gap-12 md:grid-cols-2">
              <div>
                <h2 className="text-4xl font-bold leading-tight">
                  Como o UNIQUE <br />
                  transforma
                </h2>
                <p className="mt-6 text-gray-400 leading-relaxed">
                  O UNIQUE é a solução PDV e delivery que sua loja precisa. Com funcionalidades intuitivas, oferecemos uma forma como seus gerentes de negócio têm total controle de forma simples e eficaz.
                </p>
                <p className="mt-4 text-gray-400 leading-relaxed">
                  Além disso, o UNIQUE oferece soluções eficientes de entrega que agilizam seus pedidos, melhorando a experiência do seu cliente. Com nossos recursos você consegue gerenciar com facilidade e escalabilidade e alcançando resultados comprovados.
                </p>
              </div>
              <div className="relative h-96">
                <Image
                  src="/unique-store.jpg"
                  alt="Como funciona UNIQUE"
                  fill
                  className="object-cover rounded-lg"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Features Cards */}
        <section className="bg-black px-4 py-20 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="grid gap-6 md:grid-cols-2">
              {/* Card 1 */}
              <Card className="border-0 bg-red-600 p-8 text-white">
                <h3 className="mb-4 text-2xl font-bold">
                  Gestão de Vendas <br />
                  Eficiente
                </h3>
                <p className="mb-6 font-semibold">
                  Acompanhe suas vendas em tempo real com histórico
                </p>
                <p className="text-sm leading-relaxed">
                  O UNIQUE permite que você gerencie todas as vendas de forma simples e eficaz, com relatórios detalhados e informações.
                </p>
              </Card>

              {/* Card 2 */}
              <Card className="border-0 bg-red-600 p-8 text-white">
                <h3 className="mb-4 text-2xl font-bold">
                  Delivery Ágil e <br />
                  Prático
                </h3>
                <p className="mb-6 font-semibold">
                  Entregas rápidas para seus clientes satisfeitos
                </p>
                <p className="text-sm leading-relaxed">
                  Com a UNIQUE, o processo de entrega é utilizado e simplificado, permitindo que você mantenha clientes satisfeitos, acompanhando a satisfação.
                </p>
              </Card>
            </div>
          </div>
        </section>

        {/* Três razões */}
        <section className="bg-black px-4 py-20 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <h2 className="mb-16 text-center text-4xl font-bold">
              Três razões para escolher UNIQUE
            </h2>
            <div className="grid gap-8 md:grid-cols-3">
              {[
                {
                  image: '/interface-intuitive.jpg',
                  title: 'INTERFACE INTUITIVA',
                  desc: 'Experiência uma navegação simples e intuitiva',
                },
                {
                  image: '/dedicated-support.jpg',
                  title: 'SUPORTE DEDICADO',
                  desc: 'Atendimento personalizado para sua loja',
                },
                {
                  image: '/real-time-reports.jpg',
                  title: 'RELATÓRIOS EM TEMPO REAL',
                  desc: 'Acompanhe dados e análises instantaneamente',
                },
              ].map((item, idx) => (
                <div key={idx} className="text-center">
                  <div className="relative mb-6 h-48 w-full overflow-hidden rounded-lg">
                    <Image
                      src={item.image}
                      alt={item.title}
                      fill
                      className="object-cover"
                    />
                  </div>
                  <h3 className="mb-2 text-sm font-bold tracking-wide text-gray-400">
                    {item.title}
                  </h3>
                  <p className="text-sm text-gray-400">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Por que escolher */}
        <section id="why" className="bg-black px-4 py-20 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="grid gap-12 md:grid-cols-2">
              <Card className="border-0 bg-red-600 p-8 text-white">
                <h2 className="text-3xl font-bold leading-tight">
                  Por que escolher o UNIQUE para seu negócio?
                </h2>
                <p className="mt-6 leading-relaxed">
                  O UNIQUE oferece as melhores soluções PDV e delivery necessárias com eficiência e confiabilidade.
                </p>
              </Card>

              <div className="space-y-8">
                {[
                  {
                    title: 'Facilidade de uso',
                    desc: 'O UNIQUE é intuitivo, permitindo que qualquer um o mantenha implementando.',
                  },
                  {
                    title: 'Escalabilidade',
                    desc: 'Adapte o sistema conforme seu negócio cresce e evolui com efetividade.',
                  },
                  {
                    title: 'Segurança',
                    desc: 'Protegemos seus dados com as melhores práticas de segurança disponíveis.',
                  },
                ].map((item, idx) => (
                  <div key={idx} className="border-b border-gray-800 pb-6">
                    <h3 className="text-lg font-bold">{item.title}</h3>
                    <p className="mt-2 text-gray-400">{item.desc}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* CTA Final */}
        <section id="contact" className="bg-black px-4 py-20 sm:px-6 lg:px-8">
          <div className="relative mx-auto max-w-4xl overflow-hidden">
            {/* Decorative element */}
            <div className="absolute right-0 bottom-0 h-48 w-48 text-white opacity-5">
              <svg viewBox="0 0 100 100" fill="none" stroke="currentColor" strokeWidth="1">
                <circle cx="50" cy="50" r="40" />
                <path d="M 30 50 Q 50 30 70 50" />
              </svg>
            </div>

            <div className="relative text-center">
              <h2 className="text-balance text-4xl font-bold">
                Transforme suas <br />
                vendas hoje!
              </h2>
              <p className="mt-4 text-gray-400">
                Descubra como o UNIQUE pode revolucionar
              </p>
              <Button asChild className="mt-8 bg-red-600 hover:bg-red-700 text-white">
                <Link href="#contact">COMECE AGORA</Link>
              </Button>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="border-t border-gray-800 bg-black px-4 py-8 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-6xl">
            <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
              <div>
                <h3 className="text-lg font-bold">UNIQUE</h3>
              </div>
              <p className="text-sm text-gray-400">
                Siga-nos: @reallygreatsite
              </p>
            </div>
          </div>
        </footer>
      </main>
    </>
  )
}
