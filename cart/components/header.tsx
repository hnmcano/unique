"use client"

import { Button } from "@/components/ui/button"
import { Menu, X } from "lucide-react"
import { useState } from "react"
import Link from "next/link"

export function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <nav className="container flex h-16 items-center justify-between px-4">
        <div className="flex items-center gap-2">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-foreground">
          <img src="/apple-icon.png" style={{ maxWidth: "80%"}} alt="Unique"/>
          </div>
          <span className="text-xl font-bold text-foreground">UNIQUE</span>
        </div>

        <div className="hidden items-center gap-8 md:flex">
          <a
            href="#recursos"
            className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Recursos
          </a>
          <a
            href="#depoimentos"
            className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Depoimentos
          </a>
          <a
            href="#precos"
            className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors"
          >
            Preços
          </a>
        </div>
        <div className="hidden items-center gap-4 md:flex">
          <Link href="/login">
            <Button variant="ghost" size="sm">
              Entrar
            </Button>
          </Link>
          <Link href="/register">
            <Button size="sm" className="bg-primary text-primary-foreground hover:bg-primary/90">
              Começar Grátis
            </Button>
          </Link>
        </div>

        <button className="md:hidden" onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
          {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </nav>
      {mobileMenuOpen && (
        <div className="border-t border-border bg-background md:hidden">
          <div className="container space-y-4 px-4 py-6">
            <a href="#recursos" className="block text-sm font-medium text-muted-foreground hover:text-foreground">
              Recursos
            </a>
            <a href="#depoimentos" className="block text-sm font-medium text-muted-foreground hover:text-foreground">
              Depoimentos
            </a>
            <a href="#precos" className="block text-sm font-medium text-muted-foreground hover:text-foreground">
              Preços
            </a>
            <div className="flex flex-col gap-2 pt-4">
              <Link href="/login">
                <Button variant="outline" size="sm" className="w-full bg-transparent">
                  Entrar
                </Button>
              </Link>
              <Link href="/register">
                <Button size="sm" className="w-full bg-primary text-primary-foreground">
                  Começar Grátis
                </Button>
              </Link>
            </div>
          </div>
        </div>
      )}
    </header>
  )
}
