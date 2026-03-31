"use client"

import { useState } from "react";
import MatrixRainBackground from "@/components/matrixrainbackground"

export default function RegisterFormulation() {
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            alert("As senhas não coincidem. Por favor, tente novamente.");
            return;
        }
    };

    return (
        <section className="relative bg-black py-20 md:py-32 min-h-screen flex items-center overflow-hidden">
            <MatrixRainBackground />
            <div className="container px-10 relative z-10">
                <form className="mx-auto max-w-md bg-background p-8 rounded-lg shadow-md">
                    <div className="mb-4">
                        <label htmlFor="name" className="block text-sm font-medium text-muted-foreground">
                            Nome
                        </label>
                        <input
                            type="text"
                            id="name"
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Seu nome"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="email" className="block text-sm font-medium text-muted-foreground">
                            Email
                        </label>
                        <input
                            type="email"
                            id="email"
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="seu.email@exemplo.com"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="password" className="block text-sm font-medium text-muted-foreground">
                            Senha
                        </label>
                        <input
                            type="password"
                            id="password"
                            onChange={(e) => setPassword(e.target.value)}
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Sua senha"
                        />
                    </div>
                    <div className="mb-4">
                        <label htmlFor="confirm-password" className="block text-sm font-medium text-muted-foreground">
                            Confimar Senha
                        </label>
                        <input
                            type="password"
                            id="confirm-password"
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            className="mt-1 block w-full rounded-md border border-input bg-background py-2 px-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                            placeholder="Confirme sua senha"
                        />
                    </div>
                    <div className="mb-4">
                        { confirmPassword !== password && 
                            <p className="text-sm text-red-500">
                                As senhas não coincidem
                            </p> 
                        }
                    </div>
                    <div className="mb-4">
                        <label className="inline-flex items-center">
                            <input type="checkbox" className="rounded border-input text-primary focus:ring-primary" />
                            <span className="ml-2 text-sm text-muted-foreground">
                                Concordo com os <a href="#" className="text-primary hover:underline">Termos de Serviço</a> e a <a href="#" className="text-primary hover:underline">Política de Privacidade</a>.
                            </span>
                        </label>
                    </div>
                    <button
                        type="submit"
                        onClick={handleSubmit}
                        className="w-full bg-primary text-primary-foreground hover:bg-primary/90 py-2 px-4 rounded-md shadow-md transition-colors duration-200"
                    >
                        Criar Conta
                    </button>
                </form>
            </div>
        </section>
    )
}